# Métodos e Funções de Listas

#Metodos de listas

lista = [1,3,12,8,2]

#append - no final da lista
print ("Antes do append", lista)

lista.append(3)

print("Depois do append", lista)

#insert - escolhe qual e onde você inclui

lista.insert(2,10)

print("Depois o insert" , lista)

#extend - juntar duas listas

lista2 = [1,2,3]
lista.extend(lista2)

print ("Depois do extend", lista)

#pop - remover o elemento, se nao for especificado retira o ultimo elemento

lista.pop()

print("Lista após o pop:", lista)

lista.pop(0)

print("Lista após o pop2:", lista)

#remove - retirar item da lista, sempre o primeiro encontrado

lista.remove(3)

print("Depois do remove", lista)

#count 

print("Quantidade de 2 na lista" , lista.count(2))

#index

print("Qual o indice do elemento 12", lista.index(12))

#sort
lista.sort()

print(lista)

lista.sort(reverse=True)

print(lista)

#Funções para listas

#lenght (len)

print(len(lista))

#sum

print(sum(lista))

#max e min - menor valor e menor valor da lista
 
print("Maior elemento da lista", max(lista))
print("Menor elemento da lista", min(lista))
