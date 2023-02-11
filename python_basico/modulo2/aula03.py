choop = float(input("Digite quantos Choops voce tomou na Ocktober:> "))

if choop  == 0:
    print("Voce nao bebeu!!")

#multa = choop * 100 
elif choop >= 1 and choop <=5 :
    print("voce ja esta entrando na zona de risco!")
    
    multa = choop * 100
    
elif  choop > 5 :
    multa = choop * 100
    print(f"voce ja esta alterado e foi multado em {multa}")
    
    

