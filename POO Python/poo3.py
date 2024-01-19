class gato:
    def __init__(self, nome:str,raca:str,peso:float, idade:int, castrado:bool):
        self.nome = nome
        self.raca= raca
        self.peso = peso
        self.idade = idade
        self.castrado = castrado
    def miar(self):
        return f'O {self.nome} está miando, dê atenção à ele.'
    

gato1 =gato(nome="Catarina", raca="Laranja",peso=1.70,idade=2,castrado=False)
gato2 = gato(nome="porra espermeada", raca="gala",peso=1.40,idade=12,castrado=True)

print(gato2.miar())
print(gato1.miar())
