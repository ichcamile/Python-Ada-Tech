#04. Operadores Aritméticos e Booleanos

"""
Soma: +
Subtração: -
Multiplicação: *
Divisão: /
Divisão Inteira: //
Resto da divisão: %
Potência: **
 
"""

numero1 = 10
numero2 = 20

print (numero1 + numero2)
print (numero1 - numero2)
print (numero1 * numero2)
print (numero1 / numero2)

print (numero1 // numero2)
#divisão acima é inteira, então descarta a parte decimal

#operador de mod = % (20% 3)
print (20 % 3)
#vinte mod 3 - operador de modulo - resto da divisão
print (2**3)
print (20//3) 
#divisão acima daria 6,666


#OPERADORES BOLEANOS - OPERADORES LOGICOS - COMPARAÇÃO
idade1 = 10 
idade2 = 15
altura1 = 1.77
altura2 = 1.65
altura3 = altura2

print (idade1 > idade2) #maior que 
print (idade1 <= idade2) #menor ou igual
print ("Python" == "python") #comparação
print ("banana" != "abacaxi") #é diferente
print (altura1 >= altura2)
print (altura2 > altura3)