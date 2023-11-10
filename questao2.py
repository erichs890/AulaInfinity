def crieUmaFuncaoQueRetornaQuantasLetrasPossuiUmaPalavraSeForPassadoUmaFraseAFuncaoDeveraRetornarONumeroDeLetrasEsoacosVaziosEQuatosSinaisDePontuacao(palavra):
    palavra = palavra.lower().strip()
    numero_de_letras = 0
    numero_de_espacos = 0
    numero_de_pontuacoes = 0
    if " " in palavra:
        for letra in palavra:
            if letra == " ":
                numero_de_espacos+=1
            elif letra in "abcdefghijklmnopqrstuvwxyz":
                numero_de_letras+=1
            elif letra in ",.;:!?:":
                numero_de_pontuacoes+=1
        return f"A frase tem {numero_de_letras} letras, {numero_de_espacos} espaços e {numero_de_pontuacoes} pontuações"
    else:
        return len(palavra)

vish = str(input("DIZ AI PAIZIN: ")).strip()
print(crieUmaFuncaoQueRetornaQuantasLetrasPossuiUmaPalavraSeForPassadoUmaFraseAFuncaoDeveraRetornarONumeroDeLetrasEsoacosVaziosEQuatosSinaisDePontuacao(vish))