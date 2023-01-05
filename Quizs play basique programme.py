class quiz:
    def __init__(self,questions,rep,repcorr,point):
        self.questions=questions
        self.rep=rep
        self.repcorr=repcorr
        self.point=point
        
    def affichequestion(self,numeros):
        print (self.questions[numeros] )
    
    def afficherep(self,numeros):
        print (self.rep[numeros])
    
    def afficherepcorrect(self,numeros):
        print (self.repcorr[numeros])
    
    def donner_une_rep(self):
        reponse_user=input('reponse')
        #print (reponse_user)
        return reponse_user


    def comparaison_rep(self,rep_user,numeros):
        if rep_user==self.repcorr[numeros]:
            print(True)
            return True

        else:
            print(False, "True answer is")
            self.afficherepcorrect(numeros)    


    
    def partie(self,score=0):
        for k in range(0,len(self.nom_questions)):
            self.affichequestion(k)
            self.afficherep(k)
            r=self.donner_une_rep
            self.comparaison_rep(r,k)
            if self.comparaison_rep(r,k)==True:
                score=score+self.point
        print(score)
    
    def __str__(self):
        return self.rep, self.questions
    
    def __repr__(self):
        return self.__str__()
            


testquestions = ['q1', 'Q2']
testrep = [['r11', 'r21'], ['r21', 'r22', 'r23', 'r24']]
testrepcorr = [[0,1], [0,0,1,0]]
testpoint=[[1], [2]]

testquiz=quiz(testquestions,testrep,testrepcorr,testpoint)
testquiz.comparaison_rep([0,1],0)