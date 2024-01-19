class Veiculo:
    def __init__(self, marca: str, modelo: str, ano: int, cor: str):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    def ligar(self):
        return f"O veiculo {self.modelo} ligou"
    
class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, cor: str,qntPortas: int):
        super().__init__(marca, modelo, ano, cor)
        self.qntPortas =  qntPortas
    def cavaloPau(self):
        return f'O carro {self.modelo} que tem {self.qntPortas} portas fez um cavalo de pau'



class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, cilindradas):
        super().__init__(marca, modelo, ano, cor)
        self.cilindradas = cilindradas
    def empinar(self):
        return f'A moto {self.modelo} de {self.cilindradas} cilindradas está empinando'
    
carro1 = Carro(marca= "nao",modelo="nao",ano=1, cor="nao",qntPortas=5)
moto1 = Moto(marca="sim", modelo="sim", ano=2 , cor= "sim", cilindradas= 3)
print(carro1.ligar())
print(carro1.cavaloPau())

print(moto1.ligar())
print(moto1.empinar())