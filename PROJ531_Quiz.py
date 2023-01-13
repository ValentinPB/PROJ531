##PROJ531 Quiz

#Ce code ci-dessous récupère le chemin des fichiers sur n'importe quelle machine
import os
from inspect import getsourcefile
path = os.path.abspath(getsourcefile(lambda:0))
path = path[::-1]
c = 0
while path[c] != '\\' :
    c = c+1
for i in range(c) :
    path = path.replace(path[0], '', 1)
path = path[::-1]
path = path + 'Quizs\\'


#Lecture du fichier
def ExploitationFichier(titre) :
    fileInfo = path + titre + '.txt'
    with open(fileInfo) as q :
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
    return(titre, questions, reponses, reponsescorrectes, scores, timers)


#Affichage des informations du Quiz :
def LectureFichier(titre) :
    files = []
    for root, dirs, files in os.walk(path):     #parcours de tous les fichiers dans le dossier Quizs
        for name in files:
            #print(name)
            if name.endswith((".txt")):         #Ajout de tous les fichiers qui se terminent par .txt
                files.append(name)
            break
        break
    if titre + '.txt' not in files :            #vérification de l'existence du fichier
        print("Ce fichier n'existe pas.")
    else :
        titre, questions, reponses, reponsescorrectes, scores, timers = ExploitationFichier(titre)
        print('Le titre du quiz est : ', titre, '\nLes questions sont : ', questions, '\nLes réponses sont : ', reponses, '\nLes réponses correctes sont : ', reponsescorrectes, '\nLes scores des questions sont : ', scores, '\nLes timers des questions sont : ', timers)


#Vérification d'incohérences :
def VerifIncoherences(titre) :
    files = []
    for root, dirs, files in os.walk(path):         #Vérification d'existence
        for name in files:
            #print(name)
            if name.endswith((".txt")):
                files.append(name)
            break
        break
    if titre + '.txt' not in files :
        print("Ce fichier n'existe pas.")
    else :
        titre, questions, reponses, reponsescorrectes, scores, timers = ExploitationFichier(titre)
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
            print('Attention : le nombre de timers ne correspond pas au nombre de questions.')
            bon = False             #On a détecté une incohérence.

        if bon :        #Si aucun problème n'a été detecté.
            print('Aucun problème détecté.')
