alunos = []
def cadastrarAluno():
    numero = 0
    nome = str(input("Diz o nome do aluno: \n"))
    cpf = input("Diz teu cpf do aluno: \n")
    while not cpf.isdigit():
        print("CPF DEVE TER APENAS NUMEROS. TENTE NOVAMENTE")
        cpf = input("Cpf do aluno: \n")
    turma = int(input("De qual turma o aluno é ? (1 ou 2)\n"))
    notas = []
    for nota in range(4):
        nota = float(input("Diga a nota do aluno: \n"))
        notas.append(nota)
    numero += 1
    aluno = {
        "nome":nome,
        "cpf":cpf,
        "turma":turma,
        "nota":nota,
        "numero" : numero
    }
    print("Aluno cadastrado com exito!")
    alunos.append(aluno)
def visualizarAluno():
    for aluno in alunos:
        print("\nNome", aluno ["nome"])
        print("\nCpf", aluno ["cpf"])
        print("\nTurma", aluno ["turma"])
        print("\nNumero", aluno["numero"])
        for i, nota in enumerate(aluno["notas"], start=1):
            print(f"Nota {i} : {nota}")
def deletarAluno():
    matador = int(input("Qual numero do aluno q voce quer remover: \n"))
    alunos.remove(matador -1)
    print("Aluno eliminado com sucesso! ;)")
while True:
    menuzin = int(input( "1 - Cadastrar aluno \n2 - Visualizar alunos cadastrados \n3 - Deletar alunos \n4 - Sair \n"))
    match menuzin:
        case 1:
            cadastrarAluno()
        case 2:
            visualizarAluno()
        case 3:
            deletarAluno()
        case 4:
            break
        case _:
            print("Vish paizin digita uma das opções ai")