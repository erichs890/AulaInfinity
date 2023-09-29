turno = input("estuda qual serie [M, V OU N]")
match turno:
    case 'M':
        print("Bom dia")
    case "V":
        print("Boa tarde")
    case "N":
        print("Boa noite")
    case _:
        print("Valor invalido")