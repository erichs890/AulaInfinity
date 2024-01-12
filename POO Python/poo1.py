class Carro:
    def __init__(self, marca, cor, modelo, ano,qtdePorta):
        self.marca = marca
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.qtdePorta = qtdePorta
    def ligar(self):
        return f"O {self.modelo} ligou"
    def verInfo(self):
        return f"""
        Marca: {self.marca}
        Modelo: {self.modelo}
        Cor: {self.cor}
        Quantidade de portas: {self.qtdePorta}        
        """

carro1 = Carro(marca="merda",cor="merda",modelo="merda",ano="merda",qtdePorta="merda")



print(carro1.ano)
print(carro1.ligar())
print(carro1.verInfo())