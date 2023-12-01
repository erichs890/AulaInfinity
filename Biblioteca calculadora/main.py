from calculadoraBasica import *
numero1 = int(input("Diz um numero comedia: "))
numero2 = int(input("Diz um numero comedia: "))
print("Quer oq fofa? \n 1 - Adição \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão")
menu = int(input(" "))
match menu:
    case 1:
        print(soma(numero1, numero2))
    case 2:
        print(sub(numero1, numero2))
    case 3:
        print(mul(numero1,numero2))
    case 4:
        print(div(numero1,numero2))