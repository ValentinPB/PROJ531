import tkinter as tk
#import utilisateurs on importe le fichier python d'authentification



def getEntry():
    Id = entree_name.get()
    mdp = password_entry.get()
    return (Id)


app= tk.Tk ()
obj = tk.Label(text = "bonjour")

name_user = tk.Label( text ="nom d'utilisateur")
name_user.pack()
entree_name = tk.Entry()
entree_name.pack()
psw= tk.Label(text = "mot de passe")
password_entry = tk.Entry()
psw.pack()
password_entry.pack()

bouton_connexion = tk.Button(text= "connexion", command=getEntry)
bouton_connexion.pack()

obj.pack()
obj.place(x=10, y=50)
app.geometry("800x900")

app.mainloop()

