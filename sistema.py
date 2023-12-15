from tkinter import *


caixinha = Tk()
caixinha.title("FLASHBANG")
caixinha.geometry("400x400")
caixinha.configure(bg="plum")
def maiorIdade():
    if 2023 - int(nomeInput.get()) >= 18:
        print("Maior de idade")
    else: 
        print("menor de idade")


nome = Label(text = "Diz o ano q tu nasceu", bg="purple",fg="white")
nome.pack()

nomeInput = Entry() 
nomeInput.pack()

botao = Button(caixinha , text="Eviar", command=maiorIdade)
botao.pack()




caixinha.mainloop()