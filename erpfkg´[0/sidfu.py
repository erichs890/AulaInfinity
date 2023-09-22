nome = str(input("DIZ TEU NOME AÍ COMÉDIA: "))
idade = int(input("DIZ TUA IDADE AÍ COMÉDIA: "))
if idade <= 19:
    print(f"Olá {nome} tu ainda tem {idade} aninhos ?")
elif idade > 20 and idade<70:
    print(f"Olá {nome} tu tem {idade} anos ? Ta ficando velho")
elif idade>=70:
    print(f"eae {nome} tu ta idoso com seus {idade} anos")