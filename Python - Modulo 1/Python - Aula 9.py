#. Laços de Repetição (For)

"""for variavel in range (11):
    print(variavel)"""


"""for variavel in range (5,11):
    print(variavel)"""

"""for variavel in range (0,12,3):
    print(variavel)
"""

"""nota1 =  float(input("Informe sua nota"))"""
 
soma = 0

for i in range(1,4):
    nota = float(input(f"Informe sua nota {i}  "))

    soma = soma + nota

print("A nota total é" , soma)

print ("Sua média é ", soma / 3)
