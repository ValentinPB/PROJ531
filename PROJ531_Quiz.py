##PROJ531 Quiz

with open('C:\Users\Valentin\Documents\GitHub\PROJ531\Quizs\QuizTest.txt') as q :
    content = q.readlines()
close(q)

print(content)


questions = [q1, Q2]
rep = [[r11, r21], [r21, r22, r23, r24]]
repcorr = [[O,1], [0,0,1,0]]

Q = [[q1, [[r11, 0], [r12, 1]]], [q2, [[r21, 0], [r22, 0], [r23, 1], [r24, 0]]]]

