from tkinter import *
bufu = Tk()
bufu.title("EITA")
bufu.geometry("800x800")

def verSePassou():
    media = (float(nota1Input.get()) + float(nota2Input.get()))/2
    if media >= 7:
        passouOuNao.configure(text="PASSOU", bg="green")
        bufu.configure(bg="green")
        nota1.configure(bg="green")
        nota2Input.configure(bg="green")

        nota2Input.configure(bg="green")


        nota2.configure(bg="green")
        botao.configure(bg="green")

    else:
         passouOuNao.configure(text="nao passou...", bg="red")
         bufu.configure(bg="red")
         nota1.configure(bg="red")
         nota1Input.configure(bg="red")
         nota2Input.configure(bg="red")

         nota2.configure(bg="red")
         botao.configure(bg="red")
         






nota1 = Label(text="Diz tua primeira nota fofo")
nota1.pack()

nota1Input = Entry()
nota1Input.pack()


nota2 = Label(text="Diz tua segunda nota fofo")
nota2.pack()

nota2Input = Entry()
nota2Input.pack()

botao = Button(bufu,text="Ver se passou", command=verSePassou)
botao.pack()

passouOuNao = Label(text="")
passouOuNao.pack()




















bufu.mainloop()