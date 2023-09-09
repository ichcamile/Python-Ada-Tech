#Estruturas Condicionais

idade = 17
if idade >= 18:
    print("você é maior de idade!")
else: 
    print("Você é menor de idade")


media = float(input("Informe sua média:"))

if media >= 7:
    print("Você foi aprovado!")
elif media >= 5:
    print("Recuperação!")
else:
    print ("Você foi reprovado")


media = 5
presenca = 100

if media >= 7 and presenca >= 70:
    print ("Aprovado!")
else:
    print("Reprovado")

numero_sorteado = 79

numero_escolhido = int(input("Informe um numero entre 1 e 100:"))

if numero_sorteado == numero_escolhido: 
    print("Você acertou!")
else: 
    print("Você errou")
