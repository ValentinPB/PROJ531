from tkinter import *

class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.creer_widgets()

    def creer_widgets(self):
        question_suiv = "question"
        self.label = Label(self, text="Quizz")
        self.bouton = Button(self, text= question_suiv, command=self.question_suivante)
        self.label.pack()
        self.bouton.pack()

    def question_suivante(self):
        pass


if __name__ == "__main__":
    app = Application()
    app.geometry("800x600")
    app.mainloop()