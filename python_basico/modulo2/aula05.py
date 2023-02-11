#importacao otimizada, quando eu importo o modulo e a funcao
from random import choice
#variaveis solicitando dados
n1 = input("Digite seu nome:> ")
n2 = input("Digite seu nome:> ")
n3 = input("Digite seu nome:> ")
n4 = input("Digite seu nome:> ")

#Lista contem indice que inicia em 0
lista =[n1, n2, n3, n4]

#sorteado = choice(lista)
#indicie e a construcao da lista

print(" "*20, "Nome Sorteado", " "*20)

#print(f"{sorteado}")

# if sorteado == n1:
#     print("O nome Sorteado foi o primeiro digitado:")
# if sorteado == n2:
#         print("O nome Sorteado foi o segundo digitado:")
# if sorteado == n3:
#         print("O nome Sorteado foi o terceiro digitado:")
# if sorteado == n4:
#         print("O nome Sorteado foi o quarto digitado:")
tamanho =len(lista)
print(tamanho)
