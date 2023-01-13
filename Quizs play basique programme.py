#class quiz permettant de faire un quizz et de lancer une partie 
import time
from tkinter import *
import tkinter as tk
class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.creer_widgets()

    def creer_widgets(self):
       
        self.label = Label(self, text="Quizz")
        
        self.entry= Entry()
        self.label.pack()
        
   
    def bt1 (self,Liste):
        """
        fonction du bouton qui quand on l'appelle rajoute ou enleve un suivant si 1 est ou n'est pas dans la liste 
        """
        if 1 not in Liste:
            Liste.append(1)
        else :
            Liste.remove(1)
    def bt2 (self,Liste):
        if 2 not in Liste:
            Liste.append(2)
        else :
            Liste.remove(2)
    def bt3 (self,Liste):
        if 3 not in Liste:
            Liste.append(3)
        else :
            Liste.remove(3)
    def bt4 (self,Liste):
        if 4 not in Liste:
        
            Liste.append(4)
        else :
            Liste.remove(4)
        
    
    
        



   
class quizz:
     
    def __init__(self,questions,rep,repcorr,point,temps):
        self.questions=questions                        # liste questions 
        self.rep=rep                                    #liste de liste de réponses pour chaque questions 
        self.repcorr=repcorr                            # liste avec binaire qui indique la position des bonne réponse 
        self.point=point                                #nombre de point de la question 
        self.temps=temps                                #liste temps avec le temps max pour chaque question
   
        
       
    def affichequestion(self,numeros):
        """
        affiche la question numeros 
        """
        
     
        return  (self.questions[numeros] )
    
    def afficherep(self,numeros):
        """
        affiche les réponse proposé associé à la quesion numeros
        """
       
        return (self.rep[numeros])
    
    def afficherepcorrect(self,numeros):
        """
        affiche les bonne réponse associé à la question numeros 
        """
        Listebonnerep=[]
        for k in range(0,len(self.repcorr[numeros])):
            if self.repcorr[numeros][k]==1:
                Listebonnerep.append(k+1)
                
        
        return Listebonnerep
    def affichetemps(self,numeros):
        """
        affiche le temps max pour repondre à la question numeros 
        """
        
        return (self.temps[numeros])
    
    
        


     
    def comparaisonreponse(self,reponse_user,numerosquestion):
        """
        verifie si la réponse de l'utilisateur est correcte
        """
        if self.afficherepcorrect(numerosquestion)==reponse_user:
           
            return True
        else:
            
            return False 
    
    
    
    def partieavectemps(self):
        """
        permet de lancer une partie en prenant le temps en compte 
        """
        
        
        score=0                   #initialise score a 0 point
        for k in range(0,len(self.questions)): # fait tourner pour chaque question du quiz
            app = Application()     #fait une page 
            app.geometry("800x600")
            question= Label(app, text=self.affichequestion(k), font=("Courier", 15)) #affiche la question 
            question.config(fg='red')
            question.pack()
            reponse = Label(app, text=self.afficherep(k)) #affiche reponse posssible 
            reponse.pack()
            
            temps= Label(app, text=('vous avez ',self.affichetemps(k),'secondes')) #affiche le temps 
            temps.pack()
            
            tdepart=time.time() #variable qui lance le chronomètre 
            
            label_reponse= Label(app,text = "votre réponse") #titre indiquant les boutons sur lesquels appuyer 
            label_reponse.pack()
            
            Listerep=[] #initialise la liste des reponse choisi comme une liste vide 

           


            bouton1 = Button(app,text=('reponse 1',self.afficherep(k)[0]), command=lambda: app.bt1(Listerep)) # fait le bouton 1 qui appelle la fonction bt1 qui permet d'ajouter 1 à la liste ou supprimer si il est deja dedans 
            bouton2 = Button(app,text=('reponse 2',self.afficherep(k)[1]), command=lambda: app.bt2(Listerep)) 
            bouton3 = Button(app,text=('reponse 3',self.afficherep(k)[2]), command=lambda: app.bt3(Listerep)) 
            bouton4 = Button(app,text=('reponse 4',self.afficherep(k)[3]), command=lambda: app.bt4(Listerep)) 
                      
            bouton1.pack()
            bouton2.pack()
            bouton3.pack()
            bouton4.pack()
            
            
            boutonV=Button(app,text='validé',command=app.destroy) #bouton qui fait passer a la page suivante  
            boutonV.config(fg='green')
            boutonV.pack()
            app.mainloop() 
            
            
            Listerep.sort()   #met dans l'ordre la liste pour ne pas avoir d'erreur de comparaison 
            if self.comparaisonreponse(Listerep,k)==True : #regarde si la rep de l'utilisateur est vrai
                tfin=time.time() # temps fin pour calculer deltat
                deltat=int(tfin-tdepart) #temps que l'utilisateur a mis pour répondre
                if self.affichetemps(k)==0 :
                    """ si l'utilisateur a répondu bien répondu à une question sans temps 
                    affiche message bonne réponse avec les points gagné           """
                               
                    app = Application()
                    app.geometry("800x600")  
                        
                    
                    
                    point=int(self.point[k])#point gagné pour cette question prend en compte le temps 
                    labelbonnerep=Label(app,text='réponse correcte')
                    labelbonnerep.pack()
                    
                    labelpointGagné=Label(app,text='vous avez gagné ')
                    labelpointGagné.pack()
                    pointGagné= Label(app, text=(int(point),'points ')) 
                    
                    pointGagné.pack()
                    score=score+point #mise a jour du score de l'utilisateur 
                elif deltat<self.affichetemps(k) :
                    """
                    si l'utilisateur a répondu dans les temps pour une question avec temps 
                    affiche message avec temps mis et point gagné              """
                    app = Application()
                    app.geometry("800x600")  
                        
                    pointquestion=int(self.point[k])
                    tempsquestion=int(self.affichetemps(k))
                    point=pointquestion*(tempsquestion-deltat)/tempsquestion  #point gagné pour cette question prend en compte le temps 
                    labelbonnerep=Label(app,text='réponse correcte')
                    labelbonnerep.pack()
                    tempsmis=Label(app,text=('vous avez repondu en ',deltat,'seconde '))
                    tempsmis.pack()
                    
                    labelpointGagné=Label(app,text='vous avez gagné ')
                    labelpointGagné.pack()
                    pointGagné= Label(app, text=(int(point),'points ')) 
                    
                    pointGagné.pack()
                    score=score+point #mise a jour du score de l'utilisateur 
                    
                       
                elif deltat>self.affichetemps(k):
                    """
                    si bonne réponse mais pas dans les temps affiche message temps écoulé 
                    """
                    app = Application()
                    app.geometry("800x600")
                        
                    labeltimeout = Label(app, text='Bonne réponse mais le temps est écoulé')
                    labeltimeout.pack()
                    label0point=Label(app,text='vous avez gagné 0 point ')
                    label0point.pack()
                    
                        
            elif self.comparaisonreponse(Listerep,k)==False :
                """
                si mauavaise reponse affiche message  de mauvaise réponse et affiche la bonne réponse
                """
                app = Application()
                app.geometry("800x600")  
                    
                labelfaux= Label(app, text='faux la bonne reponse était la réponse')
                labelfaux.pack()
                bonnerepn=Label(app,text=self.afficherepcorrect(k))
                bonnerepn.pack()
                

                
                  
                   
            app.bouton = Button(app, text='suivant' , command=app.destroy) #fait un bouton suivant qui permet de changer de page et de lancer une nouvelle question 
            app.bouton.pack()
            app.mainloop()
            
            
        app = Application() #derniere page apres les question affichant le score 
        app.geometry("800x600")
        labelscore= Label(app,text='votre score est de :')
        labelscore.pack()
        score=Label(app,text=(int(score)))
        score.pack()
        app.mainloop()
        

testquestions = ["Quel animal est surnommé le meilleur ami de l'homme ?", 'Quel animal vit en Australie et se déplace en bondissant ?', 'Quel animal est le plus grand ?', 
'Quel animal peut vivre le plus vieux ?', 'Quel animal est surnommé le Roi des animaux ?', 'Quels animaux sont des symboles nationaux ?', 'Quels animaux sont fantastiques ?']
testrep = [['Perroquet', 'Chien', 'Chat', 'Poisson rouge'], ['Poisson volant', 'Crabe', 'Kangourou', 'Sanglier'], ['Giraffe', 'Baleine bleue', 'Mouche', 'Eléphant'], 
['Phasme', 'Eléphant', 'Chat', 'Tortue'], ['Baleine bleue', 'Crocodile', 'Lion', 'Gorille'], ['Aigle', 'Crocodile', 'Rouge-gorge', 'Coq'], ['Méduse', 'Licorne', 'Griffon', 'Dragon']]
testrepcorr =  [[0, 1, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [1, 0, 0, 1], [0, 1, 1, 1]]
testpoint=[30, 50, 75, 75, 30, 100, 50]
testtemps=[15, 30, 30, 30, 15, 60, 30]

testquizz=quizz(testquestions,testrep,testrepcorr,testpoint,testtemps)

testquizz.partieavectemps()
