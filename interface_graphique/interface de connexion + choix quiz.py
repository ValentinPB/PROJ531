# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 08:37:49 2023

@author: chafi
"""
import utilisateur as uti
from tkinter import *

global fenetre1, fenetre2,administrateur




    
    



def fenetre():  #c'est la fenetre d'accueil pour se connecter en etant joueur
    global fenetre1
    
    

    def test():
        global fenetre1 ,fenetre2
        Id = entree_name.get()
        mdp = password_entry.get()
        connect = uti.authentification(Id, mdp)
        
        if connect:
            fenetre1.destroy()
            choix_quiz()
        else:
            erreur = Label(fenetre1, text="nom utilisateur ou mdp erronés")
            erreur.pack()
    def test1():
        global fenetre1, auth_administrateur
        fenetre1.destroy()
        page_auth_administrateur()
        
    def test2():
        global fenetre1 , nouveau
        fenetre1.destroy()
        nouveau_compte()
        

    fenetre1= Tk ()
    fenetre1.title('QIz')
    menu= Menu(fenetre1)
    new_item = Menu(menu)
    new_item.add_command(label='admin', command=test1)
    new_item.add_separator()
    menu.add_cascade(label='Fichier' , menu=new_item)
    fenetre1.config(menu=menu)
    
    
    
    
    obj = Label(fenetre1,text = "Bonjour")
    titre= Label(fenetre1, text= "QIz", relief=RAISED, font=('broadway', 18),fg='green',wraplength=150)
    titre.pack()
    
    name_user =Label( fenetre1,text ="nom d'utilisateur")
    name_user.pack()
    entree_name = Entry(fenetre1)
    entree_name.pack()
    psw= Label(fenetre1,text = "mot de passe")
    password_entry = Entry(fenetre1)
    psw.pack()
    password_entry.pack()
    
    bouton_connexion = Button(fenetre1,text= "connexion",bg='#9E9E09', command=test)    
    bouton_connexion.pack()
    
    bouton_deco= Button(fenetre1, text="créer un compte", command=test2)
    bouton_deco.pack()
    
    obj.pack()
    obj.place(x=300, y=10 , anchor='ne')
    fenetre1.geometry("800x900")
    fenetre1.configure(bg='#1455B9')
    fenetre1.mainloop()


def nouveau_compte():
    
    def creer_nouveaux():
        global nouveau 
        Id = entree_name.get()
        mdp = password_entry.get()
        ajouter_le_compte = uti.NEW_ACCOUNT(Id, mdp)
        print('compte ajouter')
    global nouveau
    
    
    
    
    nouveau= Tk ()
    
    
    
    nouveau.title('QIz')
    menu= Menu(nouveau)
    new_item = Menu(menu)
    new_item.add_command(label='admin')
    new_item.add_separator()
    menu.add_cascade(label='Fichier' , menu=new_item)
    nouveau.config(menu=menu)
    
    name_user =Label( nouveau,text ="nom d'utilisateur")
    name_user.pack()
    entree_name = Entry(nouveau)
    entree_name.pack()
    psw= Label(nouveau,text = "mot de passe")
    password_entry = Entry(nouveau)
    psw.pack()
    password_entry.pack()
    bouton_creer= Button(nouveau,text="creer le compte",command=creer_nouveaux)
    bouton_creer.pack()
    nouveau.geometry("800x900")
    nouveau.mainloop()
    

def choix_quiz(): #c'est la fentre qui propose tout les quiz existant
    global fenetre2
    def test(): # a modifier selon quel fenetre on veut ouvrir
        global fenetre2, quiz
        fenetre2.destroy()
        page_quiz()
    def test1():          # permet de se deconnecter si la commande 'deconnexion' est appuyée 
        global fenetre2, fenetre1
        fenetre2.destroy()
        fenetre()
        
    fenetre2 = Tk()
    fenetre2.title('QIz')
    
    menu= Menu(fenetre2)
    new_item = Menu(menu)
    new_item.add_command(label='deconnexion', command=test1)
    new_item.add_separator()
    menu.add_cascade(label='Fichier' , menu=new_item)
    fenetre2.config(menu=menu)
    
    
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
    
def page_auth_administrateur(): #cette fentre permet à l'admin de se connecter 
    global auth_administrateur
    def test3():
        global auth_administrateur , admin
        Id = entree_name.get()
        mdp = password_entry.get()
        connect = uti.est_admin(Id, mdp)
        
        if connect:
            auth_administrateur.destroy()
            page_admin()
        else:
            erreur = Label(fenetre1, text="nom utilisateur ou mdp erronés")
            erreur.pack()
            
    def test4():
        global auth_administrateur, fenetre1
        auth_administrateur.destroy()
        fenetre()
        
        
            
    auth_administrateur = Tk()
    auth_administrateur.title('QIz')
    
    menu= Menu(auth_administrateur)
    new_item = Menu(menu)
    new_item.add_command(label='accueil', command=test4)
    new_item.add_separator()
    menu.add_cascade(label='Fichier' , menu=new_item)
    auth_administrateur.config(menu=menu)
    
    obj = Label(auth_administrateur,text = "Bonjour admin")
    obj.pack()
    obj.place(x=300, y=10 , anchor='ne')
    name_user =Label( auth_administrateur,text ="nom d'utilisateur")
    name_user.pack()
    entree_name = Entry(auth_administrateur)
    entree_name.pack()
    psw= Label(auth_administrateur,text = "mot de passe")
    password_entry = Entry(auth_administrateur)
    psw.pack()
    password_entry.pack()
    
    bouton_connexion = Button(auth_administrateur,text= "connexion", command=test3)    
    bouton_connexion.pack()
    

    
    auth_administrateur.geometry("800x900")
    auth_administrateur.mainloop()
    
def page_admin(): #cette fenetre permet d'ajouter des questions etc...
    global admin
    admin=Tk()
    admin.title('QIz')
    admin.geometry("800x900")
    admin.mainloop()

def page_quiz():
    global quiz
    """quiz = Tk()
    quiz.title('QIz')"""
    import Quizs_play_basique_programme as Quizs # on doit le mettre dans le meme fichier avec les _
    
if __name__ == '__main__':
    fenetre()