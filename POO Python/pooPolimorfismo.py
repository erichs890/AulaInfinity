class Animal:
    def fazerSom(self):
        pass
    class Cachorro(Animal):
        def fazerSom(self):
            return "caralho que tesao"
    

auau = Cachorro()
print(auau.fazerSom())