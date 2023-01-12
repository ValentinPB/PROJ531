#class quiz permettant de faire un quizz et de lancer une partie 
import time
from tkinter import *
import tkinter as tk
class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.creer_widgets()

    def creer_widgets(self):
        #question_suiv = "question"
        self.label = Label(self, text="Quizz")
        #self.bouton = Button(self, text= question_suiv, command=self.question_suivante)
        self.entry= Entry()
        self.label.pack()
        #self.bouton.pack()
   
    def bt1 (self):
        return [1]
    def bt2 (self):
       
        return [2]
    def bt3 (self):
      
        return [3]
    def bt4 (self):
        
        
        return [4]
        
    def btV(self):
        Tfin=time.time()
        self.destroy
        return Tfin
    



    def get_entry(self,reponse_entry):
        r=reponse_entry.get()
        self.destroy()
        print(r)
    def question_suivante(self):
        pass
class quizz:
     
    def __init__(self,questions,rep,repcorr,point,temps):
        self.questions=questions                        # liste questions 
        self.rep=rep                                    #liste de liste de réponses pour chaque questions 
        self.repcorr=repcorr                            # liste avec binaire qui indique la position des bonne réponse 
        self.point=point                                #nombre de point de la question 
        self.temps=temps                                #liste temps avec le temps max pour chaque question
    def bt1 (self):
        return Listerep.append(1)
                
    def bt2 (self):
       
        return Listerep.append(2)
    def bt3 (self):
      
        print(Listerep.append(3))
    def bt4 (self):
        
        
        return(Listerep.append(4))
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
    
    def convertir_rep_str_list(self,reponsestr):
        """
        fonction demandant à l'utilisateur de rentrer une réponse
        """
        Lint=[]
       
        for k in range(0,len(reponsestr)):
            if k%2==0:
                Lint.append(int(reponsestr[k]))
      
        return Lint
        


     
    def comparaisonreponse(self,reponse_user,numerosquestion):
        """
        verifie si la réponse de l'utilisateur est correcte
        """
        if self.afficherepcorrect(numerosquestion)==reponse_user:
           
            return True
        else:
            
            return False 
    
    def partiesanstemps(self):
        """
        permet de jouer une partie sans prendre le temps en compte 
        """
        score=0
        for k in range(0,len(self.questions)):
            self.affichequestion(k)
            self.afficherep(k)
            
            
            Reponse=self.donner_une_rep()
            
            
            if self.comparaisonreponse(Reponse,k)==True:
                score=score+int(self.point[k])
        print(score)
    
    def partieavectemps(self):
        """
        permet de lancer une partie en prenant le temps en compte 
        """
        
        
        score=0
        for k in range(0,len(self.questions)):
            app = Application()
            app.geometry("800x600")
            question= Label(app, text=self.affichequestion(k))
            question.pack()
            reponse = Label(app, text=self.afficherep(k))
            reponse.pack()
           
            temps= Label(app, text=('vous avez ',self.affichetemps(k),'seconde'))
            temps.pack()
            
            tdepart=time.time()
            
            app.label= Label(app,text = "votre réponse") 
            app.label.pack()
            
            Listerep=[]

           


            bouton1 = Button(app, text='réponse1' , command=Listerep.append(1))
            bouton2 = Button(app, text='réponse2' , command=Listerep.append(2))
            bouton3 = Button(app, text='réponse3' , command=Listerep.append(3))
            bouton4 = Button(app, text='réponse4' , command=Listerep.append(4))
            print(Listerep)
            
            print(Listerep)
            bouton1.pack()
            bouton2.pack()
            bouton3.pack()
            bouton4.pack()
            
            boutonV=Button(app,text='validé',command=app.destroy)
            boutonV.pack()
            app.mainloop()
            
            #time.sleep(2)
            
            
            if self.comparaisonreponse(Listerep,k)==True :
                tfin=time.time()
                deltat=int(tfin-tdepart)
                print(deltat,'seconde') 
                if deltat<self.affichetemps(k):
                    app = Application()
                    app.geometry("800x600")  
                        
                    pointquestion=int(self.point[k])
                    tempsquestion=int(self.affichetemps(k))
                    point=pointquestion*(tempsquestion-deltat)/tempsquestion
                    app.label=Label(app,text='vous avez repondu en ')
                    app.label.pack()
                    app.label= Label(app, text=deltat)
                    app.label.pack()
                    app.label=Label(app,text='seconde ')
                    app.label.pack()
                    app.label=Label(app,text='vous avez gagné ')
                    app.label.pack()
                    app.label= Label(app, text=point)
                    app.label.pack()
                    app.label=Label(app,text='point ')
                    score=score+point
                    app.mainloop()
                       
                elif deltat>self.affichetemps(k):
                    app = Application()
                    app.geometry("800x600")
                        
                    app.label = Label(app, text='temps écoulé')
                    app.label.pack
                    app.label=Label(app,text='vous avez gagné 0 point ')
                    app.label.pack()
                    app.mainloop() 
                        
            elif self.comparaisonreponse(Listerep,k)==False :
                app = Application()
                app.geometry("800x600")  
                    
                app.label= Label(app, text='faux la bonne reponse était')
                app.label.pack()
                app.label=Label(app,text=self.afficherepcorrect(k))
                app.label.pack()
                
                  
                   
            app.bouton = Button(app, text='suivant' , command=app.destroy)
            app.bouton.pack()
            app.mainloop()
            
            
        app = Application()
        app.geometry("800x600")
        app.label= Label(app,text='votre score est de :')
        app.label.pack()
        score=Label(app,text=(int(score)))
        score.pack()
        app.mainloop()
        

testquestions = ['q1', 'Q2']
testrep = [['r11', 'r21'], ['r21', 'r22', 'r23', 'r24']]
testrepcorr = [[1,1,0,0], [1,1,1,1]]
testpoint=[50, 70]
testtemps=[10,10]

testquizz=quizz(testquestions,testrep,testrepcorr,testpoint,testtemps)

"""def test():
    r=reponse_entry.get()
    app.destroy()
    print(r)"""
testquizz.partieavectemps()
"""app = Application()
reponse_entry = Entry()
reponse_entry.pack()
r=reponse_entry.get()

print(r)
app.bouton = Button(app, text='suivant' , command=test)
app.bouton.pack()
app.mainloop()
print(r)"""
