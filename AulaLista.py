# # FacaUmProgramaQuePossuaUmaListaDe5FrutasASuaEscolhaEDepoisTroqueOTerceiroItemDessaListaPorMelancia = ["Hamburger", "Tua mae", "Jiboia", "Lente do oraculo", "Rabadon"]
# # FacaUmProgramaQuePossuaUmaListaDe5FrutasASuaEscolhaEDepoisTroqueOTerceiroItemDessaListaPorMelancia [2]= "Melancia"
# # print(FacaUmProgramaQuePossuaUmaListaDe5FrutasASuaEscolhaEDepoisTroqueOTerceiroItemDessaListaPorMelancia)

# #Meu jeito
FacaUmProgramaQuePedeONomeDe5PessoasEAdicionaEssas5PessoasEmUmaListaENoFinalMostraEssaLista = []
contador = 0
while True:
    nome = str(input("DIZ AI: "))
    FacaUmProgramaQuePedeONomeDe5PessoasEAdicionaEssas5PessoasEmUmaListaENoFinalMostraEssaLista.append(nome)
    contador +=1
    if contador == 5:
        print(FacaUmProgramaQuePedeONomeDe5PessoasEAdicionaEssas5PessoasEmUmaListaENoFinalMostraEssaLista)
        break
while True:
    lane = int(input("Digite uma posição da lista: "))
    if lane >= 5:
        print("Bota um numero ate 4 ")
    else:
        nome2 = str(input("Digite um nmoe para por na posição escolhida: "))
        FacaUmProgramaQuePedeONomeDe5PessoasEAdicionaEssas5PessoasEmUmaListaENoFinalMostraEssaLista.insert(lane,nome2)
        print(FacaUmProgramaQuePedeONomeDe5PessoasEAdicionaEssas5PessoasEmUmaListaENoFinalMostraEssaLista)
        break
ZA_HANDO = int(input("Quer papocar quem ? "))
FacaUmProgramaQuePedeONomeDe5PessoasEAdicionaEssas5PessoasEmUmaListaENoFinalMostraEssaLista.pop(ZA_HANDO)
papocado = FacaUmProgramaQuePedeONomeDe5PessoasEAdicionaEssas5PessoasEmUmaListaENoFinalMostraEssaLista.pop()
print(FacaUmProgramaQuePedeONomeDe5PessoasEAdicionaEssas5PessoasEmUmaListaENoFinalMostraEssaLista)
print(f'O caboco papocado foi o {papocado}')


# #Jeito Abel
# lista = []
# for i in range(5):
#     nome = str(input("Diz um nome: "))
#     lista.append(nome)
# print(lista)
