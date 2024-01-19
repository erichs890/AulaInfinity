class Funcionario:
    def __init__(self, nome: str, cpf: str, idade: int):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
    def baterPonto(self, horario):
        return f'O funcionario {self.nome} bateu o ponto no horário {horario}'
    
class Gerente(Funcionario):
    def __init__(self, nome: str, cpf: str, idade: int):
        super().__init__(nome, cpf, idade)
    def demitir(self):
        return "O gerente demitiu alguém"
    def contratar(self):
        return "O gerente contratou alguém"
    
class Caixa(Funcionario):
    def __init__(self, nome: str, cpf: str, idade: int, numCaixa: int):
        super().__init__(nome, cpf, idade)
        self.numCaixa = numCaixa
    def fecharCaixa(self):
        return f'O caixa {self.nome} fechou o caixa {self.numCaixa}'
    


Cleber  = Funcionario(nome= "Cleber", cpf= "Cancelado", idade=40)
Sergio = Gerente(nome="Sérgio", cpf="123.122.444-00", idade=55)
Alessandra = Caixa(nome="Alessandra", cpf="123456654", idade=23, numCaixa= 1)

print(Cleber.baterPonto(8.40))
print(Sergio.baterPonto(8.00))
print(Sergio.contratar())
print(Sergio.demitir())
print(Alessandra.baterPonto(8.01))
print(Alessandra.fecharCaixa())
print("Hello World!")