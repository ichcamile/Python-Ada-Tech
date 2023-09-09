#Estruturas de listas

#Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

#com listas - abert
notas = [7.9,9.7, 8.2]

#criando listas

lista = []
lista = list()
lista = [26, "camile", 3.1415, False]
lista_de_listas = [10, [7.9,9.7, 8.2]]

""""#Indexação e Slies (fatiament)

lista = [26, "camile", 3.1415, False]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])"""

#Slices

lista = [10,20,30,40,50]
print (lista[0:3])
print (lista[3:6])
print (lista[2:])
print (lista[2:6:2])

#Interaçções com for

#1. utlizando os proprios elementos dela
for elemento in lista:
    print (elemento)

#2. utilizando os indices

print ("Comprimento da lista", len(lista))

for i in range (len(lista)):
    print(lista[i]) #imprime cada elemento da lista
