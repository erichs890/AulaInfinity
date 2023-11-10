def sim(v,h):
    return v/h
valor = float(input("Ganha quanto: "))
hora = int(input("Trabaia por quantas horas: "))
trabaio = sim(valor, hora)
print(f"tu ganha {trabaio} por hora")