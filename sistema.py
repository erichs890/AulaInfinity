from tkinter import *


caixinha = Tk()
caixinha.title("FLASHBANG")
caixinha.geometry("400x400")
caixinha.configure(bg="plum")
def maiorIdade():
    if 2023 - int(nomeInput.get()) >= 18:
        resultado.configure(text="Maior de idade")
        print("Maior de idade")
    else: 
        resultado.configure(text="Menor de idade")
        print("Menor de idade")


nome = Label(text = "Diz o ano q tu nasceu", bg="purple",fg="white")
nome.pack()

nomeInput = Entry() 
nomeInput.pack()

botao = Button(caixinha , text="Eviar", command=maiorIdade)
botao.pack()

resultado = Label(text="Resposta: ")
resultado.pack()




caixinha.mainloop()
