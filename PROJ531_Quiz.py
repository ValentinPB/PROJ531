##PROJ531 Quiz

#Lecture du fichier
with open(r'C:\Users\Valentin\Documents\GitHub\PROJ531\Quizs\QuizTest.txt') as q :
    content = q.readlines()     #Enregistrement de ce qui a été lu
q.close

#print(content[0])      #Permet d'afficher ce qui a été lu

#Séparation et assignation des différents éléments :
titre, questions, rep, repcorr, scores, timers = content[0].split(';')

questions = questions.split(',')    #Création de la liste des questions

scores = scores.split(',')          #Création de la liste des scores
for i in range(len(scores)) :       #Changement des scores en entiers
    scores[i] = int(scores[i])

timers = timers.split(',')          #Création de la liste des timers
for i in range(len(timers)) :       #Changement des timers en entiers
    timers[i] = int(timers[i])

reponses = []                       #Initialisation de la liste des réponses
rep = rep.split(',')                #Séparation des réponses en classifiant par question
for i in rep :
    #print(reponses)                    #Permet d'afficher ce qui se passe à chaque passage dans la boucle
    #print(i.split('.'))
    reponses.append(i.split('.'))   #Création de la liste des réponses

reponsescorrectes = []                                              #Initialisation de la liste des corrections
repcorr = repcorr.split(',')                                        #Séparation des corrections en classifiant par question
for i in repcorr :
    reponsescorrectes.append(i.split('.'))                          #Création de la liste des corrections
for i in range(len(reponsescorrectes)) :
    for j in range(len(reponsescorrectes[i])) :
        reponsescorrectes[i][j] = int(reponsescorrectes[i][j])      #Changement des corrections en entiers


#Affichage des informations du Quiz :
print('Le titre du quiz est : ', titre, '\nLes questions sont : ', questions, '\nLes réponses sont : ', reponses, '\nLes réponses correctes sont : ', reponsescorrectes, '\nLes scores des questions sont : ', scores, '\nLes timers des questions sont : ', timers)


#Vérification d'incohérences :
bon = True          #Cette variable permet de savoir s'il y a au moins une incohérence.
checklots = True
if len(questions) != len(reponses) :        #Verification de la cohérence entre le nombre de questions et de lots de réponses.
    print('Attention : le nombre de questions ne correspond pas au nombre de réponses.')
    bon = False             #On a détecté une incohérence.
if len(reponses) != len(reponsescorrectes) :        #Verification de la cohérence entre le nombre de lots de réponses et de lots de corrections
    print('Attention : le nombre de réponses ne correspond pas au nombre de corrections.')
    bon = False             #On a détecté une incohérence.
    checklots = False
if checklots :
    for i in range(len(reponses)) :
        if len(reponses[i]) != len(reponsescorrectes[i]) :      #Vérification de la cohérence entre le nombre de réponses par lot et de corrections par lot.
            print('Attention : Les corrections de la réponse n°', i, ' ne sont pas au bon nombre.')
            bon = False     #On a détecté une incohérence.
if len(questions) != len(scores) :      #Verification de la cohérence entre le nombre de questions et de scores.
    print('Attention : le nombre de scores ne correspond pas au nombre de questions.')
    bon = False             #On a détecté une incohérence.
if len(questions) != len(timers) :      #Verification de la cohérence entre le nombre de questions et de timers.
    print('Attention : le nombre de timers ne correspond pas au nombre de questions. Pour ne pas mettre de timer sur une question, mettez simplement la valeur 0.')
    bon = False             #On a détecté une incohérence.

if bon :        #Si aucun problème n'a été detecté.
    print('Aucun problème détecté.')

#=======
#with open('C:\Users\Valentin\Documents\GitHub\PROJ531\Quizs\QuizTest.txt') as q :
#    content = q.readlines()
#close(q)

#print(content)


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
            return False, "True answer is" 
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
        return self.rep
    
    def __repr__(self):
        return self.__str__()
            


            

def partiess(Questions,reponse,repc,point):
    score=0
    for k in range(0,len(Questions)):
        print(Questions[k])
        print(reponse[k])
        r=input('rep')
        print(r)
        if r==repc[k]:
            score=score+point[k]
            print (True)
        else:
            print(False)
            print('True answer is')
            print(repc[k])
    return score 
    

    






testquestions = ['q1', 'Q2']
testrep = [['r11', 'r21'], ['r21', 'r22', 'r23', 'r24']]
testrepcorr = [['0','1'], [0,0,1,0]]
testpoint=[[1], [2]]

testquiz=quiz(testquestions,testrep,testrepcorr,testpoint)


partiess(testquestions,testrep,testrepcorr,testpoint)