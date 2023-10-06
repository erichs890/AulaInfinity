palavra = str(input("Diz aí menor: "))
contagem1 = 0
contagem2 = 0
if palavra == palavra[::-1]:
    for letras in palavra:
        if letras not in "aeiouAEIOU":
            contagem1+=1
        elif letras in "aeiouAEIOU":
         contagem2 +=1
    print(f'a palavra {palavra} tem {contagem1} consoantes e {contagem2} vogais e é palindromo')
else:
    for letras in palavra:
        if letras not in "aeiouAEIOU":
            contagem1+=1
        elif letras in "aeiouAEIOU":
         contagem2 +=1
    print(f'a palavra {palavra} tem {contagem1} consoantes e {contagem2} vogais e não é palindromo')
