from tkinter import *
from PROJ531_QuizMaker import *

global Questions
Questions=[]
global L
L=[]
global Responses
Reponses=[]
global REP_Correct
REP_Correct=[]
global timer
timer=[]
global Score
Score=[]

def ajout_question():

    def valid_question():
        a = question_entre.get()
        Questions.append(a)
        Reponses.append(L)
        print(L)
        L = []
        print(Questions, Reponses)
    


    if len(Questions)==0 and question_entrez.get() != '':
        Questions.append(question_entrez.get())
        Reponses.append(L)
        print(L)
        L = []


    elif len(Questions)==0 and question_entrez.get() == '':
        erreur_pas_question = Label(frame, text="vous n'avez pas entré de question")
        erreur_pas_question.pack()

    else:

        question = Label(frame, text="Ajoutez votre question")
        question.pack()
        question_entre = Entry(frame)
        question_entre.pack()
        

        temps_a_mettre= Label(frame, text='rentrer le temps que vous voulez pour cette question')
        temps = Entry(frame)
        bouton_temps = Button(frame, text='valider_temps', command=valid_temps)
        temps_a_mettre.pack()
        temps.pack()
        bouton_temps.pack()

        points_a_mettre = Label(frame, text='combien de point souhaitez vous affecter à cette question')
        points = Entry(frame)
        bouton_point = Button(frame, text='valider points', command=valid_point)     
        points_a_mettre.pack()
        points.pack()
        bouton_point.pack()

        reponse = Label(frame,text="ajout reponse")
        reponse_possible= Entry(frame)
        reponse.pack()
        reponse_possible.pack()
        bouton_question_valide= Button(frame, text="valider question", command=valid_question(L, Questions))
        bouton_question_valide.pack()


def ajout_reponse():

    def pas_idee():
        a=reponse_possible.get()
        L.append(a)
        print(L)
        bouton_valid.destroy()

    reponse = Label(frame,text="ajout reponse")
    reponse_possible= Entry(frame)
    reponse.pack()
    reponse_possible.pack()
    a=reponse_possible.get()
    bouton_valid = Button(frame, text="valid reponse", command=pas_idee)
    bouton_valid.pack()

def getTitre():
    titre = titre_ajout.get()
    if titre == "": #or FileAlreadyExists(titre):
        fonctionne_pas = Label(frame, text="il existe déjà un quizz avec le même nom")
        fonctionne_pas.pack()
    else :
        recuperer_donner.destroy()

def valid_temps():
    le_temps = temps.get()
    if len(le_temps) == 0:
        erreur_temps_vide = Label(frame, text="vous n'avez pas définie de temps pour la question")
        erreur_temps_vide.pack()
    else:
        timer.append(le_temps)
        print(timer)
        bouton_temps.destroy()

def valid_point():
    nbr_point = points.get()
    if len(nbr_point) == 0:
        erreur_nbre_point = Label(frame, text="vous n'avez pas définie le nombre de point")
        erreur_nbre_point.pack()
    else:
        Score.append(nbr_point)
        print(Score)
        bouton_point.destroy()

root = Tk()
frame = Frame(root)
frame.pack()

#on définit des liste pour stocker les informations qui nous intéresse


#on demande à l'utilisateur de rentrez un titre du quizz
titre_quizz = Label(frame, text="Titre de votre quizz")
titre_ajout = Entry(frame)
titre_quizz.pack()
titre_ajout.pack()

recuperer_donner = Button(frame, text="valider titre", command= getTitre)
recuperer_donner.pack()

question1 = Label(frame, text="Ajoutez votre question")
question_entrez = Entry(frame)
'''
reponse = Label(frame,text="ajout reponse")
reponse_possible= Entry(frame)'''

question1.pack()
question_entrez.pack()
'''
reponse.pack()
reponse_possible.pack()'''


button_ajout_reponse = Button(frame, text="ajoutez des réponse", command=ajout_reponse)

temps_a_mettre= Label(frame, text='rentrer le temps que vous voulez pour cette question')
temps = Entry(frame)
bouton_temps = Button(frame, text='valider_temps', command=valid_temps)
temps_a_mettre.pack()
temps.pack()
bouton_temps.pack()

points_a_mettre = Label(frame, text='combien de point souhaitez vous affecter à cette question')
points = Entry(frame)
bouton_point = Button(frame, text='valider points', command=valid_point)
points_a_mettre.pack()
points.pack()
bouton_point.pack()

button_ajout_question = Button(frame, text="ajoutez des questions", command=ajout_question)
button_ajout_reponse.pack()
button_ajout_question.pack()


root.geometry("800x600")
root.mainloop()
