##PROJ531 Quiz Création fichier

def CreateFile(titre) :
    path = r'C:\Users\Valentin\Documents\GitHub\PROJ531\Quizs'
    fileInfo = path + titre + '.txt'
    pass

def FileAlreadyExists(titre) :
    return(False)

def FillFile(titre, questions, reponses, corrections, scores, timers) :
    pass

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
        etapecorr = True
        etapesco = True
        etapetim = True
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
        print('Maintenant, écrivez les réponses aux questions ! Pour changer de question, écrivez "suivant". Si vous avez rentré toutes vos réponses, écrivez "suivant" pour passer à la suite.')
        for i in range(len(questions)) :
            print('Vous écrivez les réponses pour la question n°', i, ' : ', questions[i])
            subetaperep = True
            subreponses = []
            while subetaperep :
                r = input()
                if r == 'suivant' :
                    if len(subreponses) <= 1 :
                        print('Vous devez rentrer au moins deux réponses !')
                    else :
                        subetaperep = False
                else :
                    subreponses.append(r)
            reponses.append(subreponses)
        print('Maintenant, donnez la réponse juste pour chaque question. Ecrivez "oui" si la réponse présentée est la bonne, ou "non" si ça ne l''est pas.')
        for i in range(len(reponses)) :
            print('Pour la question : "', questions[i], '", quelle est la bonne réponse ?')
            subcorr = []
            for j in range(len(reponses[i])) :
                if j == len(reponses) - 1 :
                    print('La dernière réponse a été automatiquement désignée correcte.')
                    subcorr.append(1)
                else :
                    print('Est-ce la réponse : "', reponses[i][j], '" ?')
                    c = input()
                    if c == 'non' :
                        subcorr.append(0)
                    else :
                        subcorr.append(1)
                        break
            corrections.append(subcorr)
        print('fin temp')
        return(titre, questions, reponses, corrections)
