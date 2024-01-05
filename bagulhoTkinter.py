from tkinter import *
bufu = Tk()
bufu.title("EITA")
bufu.geometry("800x800")

def verSePassou():
    media = (float(nota1Input.get()) + float(nota2Input.get())+float(nota3Input.get()))/3
    if media < 10 and media >= 7:
        passouOuNao.configure(text="PASSOU", bg="green")
        bufu.configure(bg="green")
        nota1.configure(bg="green")
        nota2.configure(bg="green")
        nota3.configure(bg="green")
        botao.configure(bg="green")

    elif media < 7:
         passouOuNao.configure(text="nao passou...", bg="red")
         bufu.configure(bg="red")
         nota1.configure(bg="red")
         nota2.configure(bg="red")
         nota3.configure(bg="red")

         botao.configure(bg="red")
    elif media == 10:
        passouOuNao.configure(text="PASSOU COM 10 NA MEDIA", bg="blue")
        bufu.configure(bg="blue")
        nota1.configure(bg="blue")
        nota2.configure(bg="blue")
        nota3.configure(bg="blue")

        botao.configure(bg="blue")






nota1 = Label(text="Diz tua primeira nota fofo")
nota1.pack()

nota1Input = Entry()
nota1Input.pack()


nota2 = Label(text="Diz tua segunda nota fofo")
nota2.pack()

nota2Input = Entry()
nota2Input.pack()

nota3 = Label(text="Diz tua terceira nota fofo")
nota3.pack()

nota3Input = Entry()
nota3Input.pack()


botao = Button(bufu,text="Ver se passou", command=verSePassou)
botao.pack()

passouOuNao = Label(text="")
passouOuNao.pack()




















bufu.mainloop()
