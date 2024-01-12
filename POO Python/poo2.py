class Moto:
    def __init__(self, marca, modelo, cilindradas, cor):
        self.marca = marca
        self.modelo = modelo
        self.cilindradas = cilindradas
        self.cor = cor
    
moto1 = Moto(marca="merda", modelo="merda",cilindradas="merda", cor="merda")
moto2 = Moto(marca="bosta", modelo="bosta",cilindradas="bosta", cor="bosta")
moto3 = Moto(marca="mijo", modelo="mijo",cilindradas="mijo", cor="mijo")

print(moto1.marca, moto2.cilindradas, moto3.marca, moto3.modelo, moto3.cilindradas, moto3.cor)