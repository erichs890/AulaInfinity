import random
def jokenpo(p1, p2):
    ganhou = "voce ganhou"
    perdeu = "voce perdeu"
    empate = "empate"
    if p1 == "pedra" and p2 == "tesoura" or p1 == "tesoura" and p2 == "papel" or p1 == "papel" and p2 == "pedra":
        return ganhou
    elif p1 == "pedra" and p2 == "papel" or p1 == "papel" and p2 == "tesoura" or p1 == "tesoura" and p2 == "pedra":
        return perdeu
    elif p1 == p2:
        return empate
def pedeUsuario():
    return str(input("Você não tem opção. Escolha pedra, papel ou tesoura: \n"))
def maquina():
    lista = ["pedra", "papel", "tesoura"]
    return random.choice(lista)
print(jokenpo(pedeUsuario(), maquina()))