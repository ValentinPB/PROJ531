##PROJ531 Quiz Création fichier

import os
path = 'C:\\Users\\Valentin\\Documents\\GitHub\\PROJ531\\Quizs\\'

def CreateQuizFile(titre, questions, reponses, corrections, points, timers) :
    path = r'C:\Users\Valentin\Documents\GitHub\PROJ531\Quizs'
    fileInfo = path + titre + '.txt'
    pass

def FileAlreadyExists(titre) :
    #première partie de ce code n'a pas marché.
    '''path = 'C:\\Users\\Valentin\\Documents\\GitHub\\PROJ531\\Quizs\\'       #double backslashs car si backslash tout seul, tout explose.
    path.replace(path[-1], '')      #suppression des backslashs en trop
    fileInfo = path + titre + '.txt'
    print(fileInfo)
    try :
        with open(fileInfo) as wtvr :
            wtvr.close()
        return(True)
    except FileNotFoundError :
        return(False)'''
    #partie du code fonctionnelle
    files = []
    for root, dirs, files in os.walk(path):
        for name in files:
            #print(name)
            if name.endswith((".txt")):
                files.append(name)
            break
        break
    if titre + '.txt' in files :
        return(True)
    else :
        return(False)

def IsAdmin() :
    pass

def MakeQuiz() :
    titre = input('Quel est le titre du Quiz ?\n')
    if FileAlreadyExists(titre) :
        return('Erreur : ce quiz existe déjà.')
    else :
        questions = []
        reponses = []
        corrections = []
        points = []
        timers = []
        etapequestions = True
        '''etapecorr = True
        etapesco = True
        etapetim = True'''
        #Rentrée des questions :
        print('Ecrivez vos questions les unes après les autres ! Si vous avez rentré toutes vos questions, écrivez "suivant" pour passer à la suite.')
        while etapequestions :
            q = input()
            if q == 'suivant' :
                if len(questions) == 0 :
                    print('Vous devez rentrer au moins une question !')
                else :
                    etapequestions = False
            else :
                questions.append(q)
        #Rentrée des réponses :
        print('Maintenant, écrivez les réponses aux questions ! Pour changer de question, écrivez "suivant". Si vous avez rentré toutes vos réponses, écrivez "suivant" pour passer à la suite.')
        for i in range(len(questions)) :
            print('Vous écrivez les réponses pour la question n°', i, ' : ', questions[i])
            subetaperep = True
            subreponses = []
            while subetaperep :
                r = input()
                if r == 'suivant' :
                    if len(subreponses) <= 1 :      #si l'utilisateur n'a pas rentré assez de réponses
                        print('Vous devez rentrer au moins deux réponses !')
                    else :
                        subetaperep = False
                else :
                    subreponses.append(r)
            reponses.append(subreponses)
        #Rentrée des corrections :
        print('Maintenant, donnez la réponse juste pour chaque question. Ecrivez "oui" si la réponse présentée est la bonne, ou "non" si ça ne l''est pas.')
        for i in range(len(reponses)) :
            print('Pour la question : "', questions[i], '", quelle est la bonne réponse ?')
            subcorr = []
            bonnereptrouvee = False
            for j in range(len(reponses[i])) :
                if bonnereptrouvee :
                    subcorr.append(0)
                else :
                    if j == len(reponses[i]) - 1 :
                        print('La dernière réponse a été automatiquement désignée correcte.')
                        subcorr.append(1)
                    else :
                        print('Est-ce la réponse : "', reponses[i][j], '" ?')
                        c = input()
                        if c == 'non' :         #Si l'utilisateur rentre quoi que ce soit d'autre que "non", ce sera considéré comme une bonne réponse.
                            subcorr.append(0)
                        else :
                            subcorr.append(1)
                            bonnereptrouvee = True
            corrections.append(subcorr)
        #Rentreé des points :
        print('Votre quiz est bientôt fini ! Vous allez maintenant rentrer les points à gagner pour chaque question. Pour une question sans points, rentrez "0".')
        for i in range(len(questions)) :
            print('Combien de points doit rapporter la question : "', questions[i], '" ?')
            RepIsInt = False
            while not(RepIsInt) :
                try :
                    p = int(input())            #forcer l'utilisateur à rentrer un entier
                    points.append(p)
                    RepIsInt = True
                except ValueError :
                    print('Vous devez rentrer un nombre !')
        #Rentrée des timers :
        print('Pour finir, rentrez les timers de chaque question en secondes ! Pour donner un temps illimité à une question, rentrez simplement "0".')
        for i in range(len(questions)) :
            print('Quel est le timer de la question : "', questions[i], '" ?')
            RepIsInt = False
            while not(RepIsInt) :
                try :
                    t = int(input())            #forcer l'utilisateur à rentrer un entier
                    timers.append(t)
                    RepIsInt = True
                except ValueError :
                    print('Vous devez rentrer un nombre !')
        #Résultats
        print('\nParfait ! Votre quiz est terminé, voilà le récapitulatif :')
        print('Le titre du quiz est : ', titre, '\nLes questions sont : ', questions, '\nLes réponses sont : ', reponses, '\nLes réponses correctes sont : ', corrections, '\nLes scores des questions sont : ', points, '\nLes timers des questions sont : ', timers)
        print('\n')
        return(titre, questions, reponses, corrections, points, timers)
