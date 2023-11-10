def imc(peso:float, altura:float):
    return peso/(altura**2)
lista = []
for i in range(4):
    peso = float(input("Diz teu peso truta: "))
    altura = float(input("Diz tua altura truta: "))
    lista.append(imc(peso,altura))
print(lista)