import time
class quiz:
    def __init__(self,questions,rep,repcorr,point,temps):
        self.questions=questions                        # liste questions 
        self.rep=rep                                    #liste de liste de réponses pour chaque questions 
        self.repcorr=repcorr                            # liste avec binaire qui indique la position des bonne réponse 
        self.point=point                                #nombre de point de la question 
        self.temps=temps
    def affichequestion(self,numeros):
        print (self.questions[numeros] )
        return  (self.questions[numeros] )
    
    def afficherep(self,numeros):
        print (self.rep[numeros])
        return (self.rep[numeros])
    
    def afficherepcorrect(self,numeros):
        Listebonnerep=[]
        for k in range(0,len(self.repcorr[numeros])):
            if self.repcorr[numeros][k]==1:
                Listebonnerep.append(k+1)
                
        print(Listebonnerep)
        return Listebonnerep
    def affichetemps(self,numeros):
        print(self.temps[numeros],'seconde pour répondre')
        return (self.temps[numeros])
    
    def donner_une_rep(self):
        Lint=[]
        Lstr=input('réponses choisi forme n1,n2,n3')
        for k in range(0,len(Lstr)):
            if k%2==0:
                Lint.append(int(Lstr[k]))
      
        return Lint
        


     
    def comparaisonreponse(self,reponse_user,numerosquestion):
        if self.afficherepcorrect(numerosquestion)==reponse_user:
            print('oui bonne reponse')
            return True
        else:
            print('False la reponse est:')
            self.afficherepcorrect(numerosquestion)   
            return False 
    
    def partiesanstemps(self):
        score=0
        for k in range(0,len(self.questions)):
            self.affichequestion(k)
            self.afficherep(k)
            
            
            Reponse=self.donner_une_rep()
            
            
            if self.comparaisonreponse(Reponse,k)==True:
                score=score+int(self.point[k])
        print(score)
    
    def partieavectemps(self):
        score=0
        for k in range(0,len(self.questions)):
            self.affichequestion(k)
            self.afficherep(k)
            self.affichetemps(k)
            tdepart=time.time()
            
            

            if self.comparaisonreponse(self.donner_une_rep(),k)==True :
                tfin=time.time()
                deltat=int(tfin-tdepart)
                print(deltat,'seconde') 
                if deltat<self.affichetemps(k):

                    score=score+int(self.point[k])
                else:
                    print('temps écoulé')
        print(score)


testquestions = ['q1', 'Q2']
testrep = [['r11', 'r21'], ['r21', 'r22', 'r23', 'r24']]
testrepcorr = [[1,1], [0,0,1,1]]
testpoint=[1, 2]
testtemps=[10,10]

testquiz=quiz(testquestions,testrep,testrepcorr,testpoint,testtemps)

#testquiz.partiesanstemps()
testquiz.partieavectemps()