from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import os
from random import *

def quitter():
    rep=messagebox.askyesno("Sortir","Voulez vous quitter ?")
    
    if rep:
        fen.destroy()
def  interface(fen,mot):
    fen.geometry("600x450")
    fen.title("Le pendu")
    lbTitre=Label(fen,text="Jeu le pendu",font=("arial",14))
    lbTitre.place (x=200,y=0)
    cnv=Canvas(fen, width = 280, height = 350,bg="lightblue")   
    cnv.place(x=300,y=50)
    lblMot=Label(fen,textvariable=myWord,font=("arial",24,"bold"),justify='center',width=10, borderwidth=2, relief="groove")
    ax,ay=30,50
    lblMot.place(x=ax,y=ay)
   # lblMotEcho=Label(fen,text="*" * len(mot),font=("arial",24,"bold"),justify='center',width=10)
    #lblMotEcho.place(x=ax,y=ay+40)
    lblSaisi=Label(fen,text="Saisir un caractère :",font=("arial",12))
    lblSaisi.place(x=20,y=180)
    etSaisi=Entry(fen,textvariable=myChar,width=8,font=("arial",16,"bold"),justify='center')
    etSaisi.place(x=175,y=180)
    
    btnVerifier=Button(fen,text="Vérifier le caractère",width=20,height=2,bg='lightblue',fg='red',font=("arial",12,"bold"),command=verifier)
    btnVerifier.place(x=80,y=220)
    lblNb=Label(fen,textvariable=myCont,font=("courier new",16,"bold"))
    lblNb.place(x=10,y=420)
    btnVerifier=Button(fen,text="Quitter",width=10,height=2,bg='red',fg='white',font=("arial",8,"bold"),command=quitter)
    btnVerifier.place(x=500,y=410)
    return cnv 
def un(cnv):
    cnv.create_line(10,340,260,340,width=4)
    
def deux(cnv):
   # un()
    cnv.create_line(50,340,50,40,width=4)
    
def trois(cnv):
    cnv.create_line(10,40,260,40,width=4)
    cnv.create_line(50,80,100,40,width=4)
    
def quatre(cnv):
    cnv.create_line(200,40,200,80)
    
    
def cinq(cnv):
    cnv.create_oval(180,80,220,120,width=3)
    cnv.create_line(200,120,200,140,width=3)
    
def six(cnv):
   cnv.create_line(200,140,140,180,width=3)
    
    
def sept(cnv):
    cnv.create_line(200,140,260,180,width=3)
    
    
def huit(cnv):
    cnv.create_line(200,140,200,200,width=3)
    
    
def neuf(cnv):
   cnv.create_line(200,200,140,240,width=3)
    

def dix(cnv):
    cnv.create_line(200,200,260,240,width=3)
    
    
def verifier():
    global tentative,motSaisi,monMot
    xcar=myChar.get()
    if xcar=="":
        messagebox.showerror("Erreur","Saisir un caractère d'abord !!")
    elif len(xcar)>1:
        messagebox.showerror("Erreur","Il faut saisir un et un seul caractère !!")
        myChar.set("")
    else:
        myChar.set("")
        if xcar in monMot:
            for i in range (len(monMot)):
                if xcar==monMot[i]:
                    motSaisi[i]=xcar
                    
                    myWord.set("".join(motSaisi))
                   # print(motSaisi)
            if "-" not in motSaisi:
                    messagebox.showinfo("Congratulations","Bravo, vous avez trouvé en "+str(tentative))
        else:
            myChar.set("")
            tentative+=1
            messagebox.showerror("Erreur",xcar+" non présent dans le mot !!")
            myCont.set("Chances restantes : "+str(nbMax - tentative))
            dessinePendu(tentative,cnv)
            if tentative==nbMax:
                     messagebox.showinfo("Hardluck","vous n'avez pas devené le mot !!")
                     devoileMot(monMot)
            
            
            
            
        
def choixMot(fich):
    L=[]
    f=open(fich,"r")
    if (f):
        for x in f:
            L.append(x[:-1])
    f.close()
    return choice(L)
def devoileMot(mot):
    myWord.set(mot)
def dessinePendu(tenta,cnv):
    if tenta==1:
        un(cnv)
    elif tenta==2:
        deux(cnv)
    elif tenta==3:
        trois(cnv)
    elif tenta==4:
        quatre(cnv)
    elif tenta==5:
        cinq(cnv)
    elif tenta==6:
        six(cnv)
    elif tenta==7:
        sept(cnv)
    elif tenta==8:
        huit(cnv)
    elif tenta==9:
        neuf(cnv)
    elif tenta==10:
        dix(cnv)
    
    
chemin=os.getcwd()+"/mots.txt"
nbMax=10
tentative=0
fen=Tk()
myChar = StringVar() 
myChar.set("")
cnv=None
monMot=choixMot(chemin)
motSaisi=['-']*len(monMot)
myWord=StringVar()
myWord.set("".join(motSaisi))
myCont=StringVar()
myCont.set("Chances restantes : "+str(nbMax - tentative))
cnv=interface(fen,monMot)



fen.mainloop()