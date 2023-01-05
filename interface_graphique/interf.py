import tkinter as tk
app= tk.Tk ()
obj = tk.Label(text = "bonjour")

obj.pack()
obj.place(x=10, y=50)
app.geometry("800x900")

app.mainloop()

