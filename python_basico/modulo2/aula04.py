import random
#lista
n1 = input("Digite seu nome:> ")
n2 = input("Digite seu nome:> ")
n3 = input("Digite seu nome:> ")
n4 = input("Digite seu nome:> ")

lista =[n1, n2, n3, n4]

random.shuffle(lista)

print(" "*20, "Cabecalho", " "*20)

print(lista) 