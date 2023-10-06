senha = str(input("Diz tua senha ai: "))
contemNumero = False
contemMai = False
contemMin = False
contemEspecial = False
for caracteres in senha:
    if caracteres in "1234567890":
        contemNumero = True
    elif caracteres in "!@#$%¨&*()_-":
        contemEspecial = True
    elif caracteres in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        contemMai = True
    elif caracteres in "abcdefghijklmnopqrstuvwxyz":
        contemMin = True

if contemNumero == True and contemMin == True and contemMai == True and contemEspecial == True:
    print("SENHA FORTE PAIZIN")
else:
    print("FRACO")