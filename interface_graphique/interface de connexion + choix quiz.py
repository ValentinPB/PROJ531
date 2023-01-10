# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 08:37:49 2023

@author: chafi
"""
import authentification as aut
from tkinter import *
global fenetre1, fenetre2


    
    
"""def test():
    global fenetre1 ,fenetre2
    Id = entree_name.get()
    mdp = password_entry.get()
    connect = aut.authentification(Id, mdp)
    if connect:
        fenetre1.destroy()
    else:
        bjr = Label(app, text="pppppppppppppppppppppppppppp")
        bjr.pack()
    choix_quiz()"""


def fenetre():
    global fenetre1
    
    

    def test():
        global fenetre1 ,fenetre2
        Id = entree_name.get()
        mdp = password_entry.get()
        connect = aut.authentification(Id, mdp)
        if connect:
            fenetre1.destroy()
        else:
            bjr = Label(app, text="pppppppppppppppppppppppppppp")
            bjr.pack()
        choix_quiz()
    



    
    fenetre1= Tk ()
    obj = Label(fenetre1,text = "Bonjour")
    
    name_user =Label( fenetre1,text ="nom d'utilisateur")
    name_user.pack()
    entree_name = Entry(fenetre1)
    entree_name.pack()
    psw= Label(fenetre1,text = "mot de passe")
    password_entry = Entry(fenetre1)
    psw.pack()
    password_entry.pack()
    
    bouton_connexion = Button(fenetre1,text= "connexion", command=test)  #ici on doit mettre une commande qui verifie l'utilisateur avant de destroy()  
    bouton_connexion.pack()
    
    obj.pack()
    obj.place(x=10, y=10 , anchor='ne')
    fenetre1.geometry("800x900")
    
    fenetre1.mainloop()


    """fenetre1 = Tk()
    champ_label = Label(fenetre1, text="Salut !")
    champ_label.pack()
    bouton = Button(fenetre1,text="Acceuil", command=test)
    bouton.pack()
    fenetre1.mainloop()"""

def choix_quiz():
    global fenetre2
    def test():
        choix_quiz()
    fenetre2 = Tk()
    champ_label = Label(fenetre2, text="choisir un quiz")
    champ_label.place(x=10, y=10 , anchor='ne')
    champ_label.pack()
    bouton = Button(fenetre2,text="quiz1", command=test)
    bouton.pack()
    bouton2 = Button(fenetre2,text="quiz2", command=test)
    bouton2.pack()
    bouton3 = Button(fenetre2,text="quiz3", command=test)
    bouton3.pack()
    fenetre2.geometry("800x900")
    fenetre2.mainloop()
    
    
if __name__ == '__main__':
    fenetre()