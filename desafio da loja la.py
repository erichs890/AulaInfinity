import random
clientes = []
def cadastrarCliente():
    nome = str(input("Diz teu nome ai fofinho: \n"))
    cpf = input("Diz teu cpf ai fofinho: \n")
    while not cpf.isdigit():
        print("CPF DEVE TER APENAS NUMEROS. TENTE NOVAMENTE")
        cpf = input("Cpf do cliente: \n")
    valorCompra = float(input("Diz o valor da compra: \n"))
    cliente = {
        "nome":nome,
        "cpf":cpf,
        "Valor de compra":valorCompra
    }
    clientes.append(cliente)

def sortearCliente():
    numeroClientes = len(clientes)
    sorteador = random.randint(0, numeroClientes - 1)
    clienteSorteado = clientes[sorteador]
    print(f"Parabens {clienteSorteado['nome']}, cpf:{clienteSorteado['cpf']} voce foi feito de otario por ter feito uma compra no valor de {clienteSorteado['Valor de compra']}")


while True:
    cadastro = str(input("Quer cadastrar paizin (S/N) ? ")).lower().strip()
    if cadastro == "s" or cadastro == "sim":
        cadastrarCliente()
    elif cadastro == "n" or cadastro == "nao":  
        break

sortearCliente()