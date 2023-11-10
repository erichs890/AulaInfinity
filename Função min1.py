def facaUmaFuncaoQueRecebe2NumeroERetornaOMaiorDosDois(n1:int, n2:int):
   if n1>n2:
      return n1
   elif n2>n1:
      return n2
   else: 
      return "São inguais"    
numero1 = int(input("Diz um numero ai: "))
numero2 = int(input("Diz um numero ai: "))
print(facaUmaFuncaoQueRecebe2NumeroERetornaOMaiorDosDois(numero1, numero2))