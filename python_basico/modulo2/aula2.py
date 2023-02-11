n1 = float(input("Digite Sua Primeira Nota"))
n2 = float(input("Digite Sua Segunda Nota"))

media = (n1 + n2) / 2

if media < 7:
    print("Aluno nao atingiu a media sua nota foi {} ". format(media))
    
else:
    print("Aluno  atingiu a media sua nota foi {} ". format(media))