##PROJ531 Quiz

with open(r'C:\Users\Valentin\Documents\GitHub\PROJ531\Quizs\QuizTest.txt') as q :
    content = q.readlines()
q.close

print(content[0])

titre, questions, rep, repcorr = content[0].split(';')

questions = questions.split(',')

reponses = []
rep = rep.split(',')
for i in rep :
    #print(reponses)
    #print(i.split('.'))
    reponses.append(i.split('.'))

reponsescorrectes = []
repcorr = repcorr.split(',')
for i in repcorr :
    reponsescorrectes.append(i.split('.'))