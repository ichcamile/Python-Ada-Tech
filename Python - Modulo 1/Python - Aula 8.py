#08. Laços de Repetição ("While")

numero_sorteado = 79

numero_escolhido = int(input("Informe um numero entre 1 e 100:"))

while numero_escolhido != numero_sorteado:
    print("Você errou o numero, tente novamente")
    numero_escolhido = int(input("Informe um numero entre 1 e 100:"))

print ("Parabens, você acertou!!!")


"""Example 2 - counter 

contador = int(input("Qual nivel está o contador?  "))
contador1 = int(if contador <5, then )


while contador <5:
    print (contador)


print ("O Contador está atualmente neste nivel", contador1)

    

"""