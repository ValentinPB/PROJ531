##PROJ531 Quiz Création fichier

import os
path = 'C:\\Users\\Valentin\\Documents\\GitHub\\PROJ531\\Quizs\\'

def CreateQuizFile(titre, questions, reponses, corrections, points, timers) :
    fileInfo = path + titre + '.txt'
    q = open(fileInfo, "w+")
    q.write(titre)
    q.write(";")
    for i in range(len(questions)) :
        q.write(questions[i])
        if i < len(questions) - 1 :
            q.write(",")
    q.write(";")
    for r1 in range(len(reponses)) :
        for r2 in range(len(reponses[r1])) :
            q.write(reponses[r1][r2])
            if r2 < len(reponses[r1]) - 1 :
                q.write(".")
        if r1 < len(reponses) - 1 :
            q.write(",")
    q.write(";")
    for c1 in range(len(corrections)) :
        for c2 in range(len(corrections[c1])) :
            q.write(str(corrections[c1][c2]))
            if c2 < len(corrections[c1]) - 1 :
                q.write(".")
        if c1 < len(corrections) - 1 :
            q.write(",")
    q.write(";")
    for p in range(len(points)) :
        q.write(str(points[p]))
        if p < len(points) - 1 :
            q.write(",")
    q.write(";")
    for t in range(len(timers)) :
        q.write(str(timers[t]))
        if t < len(timers) - 1 :
            q.write(",")
    content = q.readlines()
    q.close
    return(content)

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
    titre = input('Quel est le titre du Quiz ? ATTENTION : Votre titre ne peut pas comporter de points-virgules.\n')
    while FileAlreadyExists(titre) :
        print('Ce quiz existe déjà ! Si vous voulez supprimer le quiz existant pour en créer un nouveau, écrivez "supprimer". Pour changer de titre, écrivez simplement votre nouveau titre. Pour annuler la création, écrivez "annuler".')
        Ntitre = input()
        if Ntitre == 'supprimer' :
            fileInfo = path + titre + '.txt'
            os.remove(fileInfo)
            print('Quiz supprimé. Vous pouvez maintenant continuer la création de votre nouveau quiz.')
        elif Ntitre == 'annuler' :
            return('Création annulée.')
        else :
            titre = Ntitre
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
    print('Ecrivez vos questions les unes après les autres ! Si vous avez rentré toutes vos questions, écrivez "suivant" pour passer à la suite. ATTENTION : Vos questions ne peuvent pas comporter de virgules NI de points-virgules.')
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
    print('Maintenant, écrivez les réponses aux questions ! Pour changer de question, écrivez "suivant". Si vous avez rentré toutes vos réponses, écrivez "suivant" pour passer à la suite. ATTENTION : Vos réponses ne peuvent pas comporter de virgules NI de points-virgules NI de points.')
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
    print('Maintenant, donnez les réponses justes pour chaque question. Ecrivez "oui" si la réponse présentée est bonne, ou "non" si elle est fausse.')
    for i in range(len(reponses)) :
        print('Pour la question : "', questions[i], '", quelle sont les bonnes réponses ?')
        subcorr = []
        AuMoinsUneJuste = False
        for j in range(len(reponses[i])) :
            if j == len(reponses[i]) - 1 and not(AuMoinsUneJuste) :
                print('La dernière réponse a été automatiquement désignée correcte.')
                subcorr.append(1)
            else :
                print('La réponse : "', reponses[i][j], '" est-elle correcte ?')
                c = input()
                if c == 'non' :         #Si l'utilisateur rentre quoi que ce soit d'autre que "non", ce sera considéré comme une bonne réponse.
                    subcorr.append(0)
                else :
                    subcorr.append(1)
                    AuMoinsUneJuste = True
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
    #Création du fichier
    CreateQuizFile(titre, questions, reponses, corrections, points, timers)
    #Résultats
    print('\nParfait ! Votre quiz est terminé, voilà le récapitulatif :')
    print('Le titre du quiz est : ', titre, '\nLes questions sont : ', questions, '\nLes réponses sont : ', reponses, '\nLes réponses correctes sont : ', corrections, '\nLes scores des questions sont : ', points, '\nLes timers des questions sont : ', timers)
    print('\n')
    return(titre, questions, reponses, corrections, points, timers)
