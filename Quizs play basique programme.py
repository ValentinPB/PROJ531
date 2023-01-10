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
    
    def donner_une_rep(self):
        
        return input('liste réponse correcte')


    def comparaison_rep(self,rep_user,numeros):
        if self.repcorr[numeros][rep_user-1]==1:
            print(True)
            return True

        else:
            print(False, "True answer is")
            self.afficherepcorrect(numeros)  
            return False  


    
    def partiebasique(self):
        score=0
        for k in range(0,len(self.questions)):
            self.affichequestion(k)
            self.afficherep(k)
            
            
            
            if self.comparaison_rep(self.donner_une_rep(k),k)==True:
                score=score+int(self.point[k])
        print(score)
    
    def __str__(self):
        return self.rep, self.questions
    
    def __repr__(self):
        return self.__str__()
            


testquestions = ['q1', 'Q2']
testrep = [['r11', 'r21'], ['r21', 'r22', 'r23', 'r24']]
testrepcorr = [[0,1], [0,0,1,1]]
testpoint=[1, 2]
testtemps=[30,45]

testquiz=quiz(testquestions,testrep,testrepcorr,testpoint,testtemps)
testquiz.afficherepcorrect(1)
r=testquiz.donner_une_rep()
print(r)
#testquiz.partie()

