#05. Conversão de Tipos

idade = "26"
numero1 = "10"
numero2 = "20"

#variaveis que viram string, ou seja texto

print( numero1 + numero2) # junção dos textos
#print (10 +numero2) #erro entre operações

print(idade, type(idade))

idade_inteira = int (idade)
print (idade_inteira, type(idade_inteira))
"""
int ()
str ()
float ()
bool ()

"""

altura = float (input ("Informe a sua altura: "))
print ("sua altura é:")
print(altura, type(altura))

#tudo no input é tipo str


num1 = 25.9

dobro = 2*num1

print("O dobro do número digitado é:", dobro)
print (dobro, type(dobro))


x = 10
y = 4.2

num = float(input("Digite um número a seguir: "))

print(num > x*y, num <= x + y, num*y != x*y)

