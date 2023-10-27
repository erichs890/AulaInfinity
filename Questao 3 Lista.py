# # Lista de produtos e preços
# produtos = [("Maçã", 2.50), ("Banana", 1.75), ("Laranja", 3.00)]

# # Inicializa a variável que irá armazenar o valor total
# total = 0

# # Itera sobre a lista de produtos
# for produto, preco in produtos:
#     print(f"{produto}: R${preco:.2f}")
#     total += preco

# # Exibe o valor total
# print(f"Valor total: R${total:.2f}")
# #Feito com o GPT

produtos = [("Maçã", 2.50), ("Banana", 1.75), ("Laranja", 3.00)]
soma = 0
for produto in produtos:
    soma += produto[1]
    print(soma)