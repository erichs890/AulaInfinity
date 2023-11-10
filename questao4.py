def soma(n1, n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
numero1 = int(input("Diz um numero comedia: "))
numero2 = int(input("Diz um numero comedia: "))
print("Quer oq fofa? \n 1 - Adição \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão")
menu = int(input(" "))
if menu == 1:
    print(soma(numero1, numero2))
elif menu == 2:
    print(sub(numero1, numero2))
elif menu == 3:
    print(mul(numero1,numero2))
elif menu == 4:
    print(div(numero1,numero2))