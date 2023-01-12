from tkinter import *

def ajout_question():
    question = Label(frame, text="Ajoutez votre question")
    question.pack()
    question_entre = Entry(frame)
    question_entre.pack()

    reponse = Label(frame,text="ajout reponse")
    reponse_possible= Entry(frame)
    reponse.pack()
    reponse_possible.pack()


def ajout_reponse():

    def pas_idee():
        a=reponse_possible.get()
        print(a, "                 p")
        L.append(a)
        print(L)
        bouton_valid.destroy()


    reponse = Label(frame,text="ajout reponse")
    reponse_possible= Entry(frame)
    reponse.pack()
    reponse_possible.pack()
    a=reponse_possible.get()
    bouton_valid = Button(frame, text="valid question", command=pas_idee)
    bouton_valid.pack()

def getEntry():
    a=ajout_reponse
    interieur_reponse = reponse_possible.get()
    interieur_question = question_entrez.get()
    L.append(interieur_question)
    print(interieur_question, "    ", interieur_reponse)
    print(L)

#
root = Tk()
frame = Frame(root)
frame.pack()
L=[]
titre_quizz = Label(frame, text="Titre de votre quizz")
titre_ajout = Entry(frame)
titre_quizz.pack()
titre_ajout.pack()
question1 = Label(frame, text="Ajoutez votre question")
question_entrez = Entry(frame)
reponse = Label(frame,text="ajout reponse")
reponse_possible= Entry(frame)

question1.pack()
question_entrez.pack()
reponse.pack()
reponse_possible.pack()


button_ajout_reponse = Button(frame, text="ajoutez des réponse", command=ajout_reponse)
button_ajout_question = Button(frame, text="ajoutez des questions", command=ajout_question)
button_ajout_reponse.pack()
button_ajout_question.pack()


recuperer_donner = Button(frame, text="recup donné", command= getEntry)
recuperer_donner.pack()
root.geometry("800x600")
root.mainloop()
