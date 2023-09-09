"""x = 4.2

y = 10

z = "42"

print (not (((x * y == z) and not (x < y)) or y % 2 == 0))


print (not (((not True) or int(z) % 7 == 0) and ((str(int(x*y)) == z) and (type(x) != type(z)))))

print ((True and True) or not True)

a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
c = int(input("Digite o terceiro número inteiro: "))
"""


"""x = int(input("Digite um número inteiro: "))

if x < 0:
    resp1 = "negativo"
else:
    resp1 = "positivo"
    
if x % 2 == 0:
    resp2 = "par"
else:
    resp2 = "impar"
    

print("O número {} é {} e {}.".format(x, resp1, resp2))"""

"""cont = 0
resultado = 0
n = 1000

while cont != n:

    resultado = resultado + 1/(2**cont)

    cont = cont + 1

print(resultado)"""


lista_inicial = [10, 5, -7, 6, -42, 63, -8, -5, 13]

lista_final = []

for item in lista_inicial:

    if item % 2 == 0:

        if item < 0:

            lista_final.append(A)
    
        else:

            lista_final.append(B)
    else:

        if item < 0:
            
            lista_final.append(C)
    
        else:

            lista_final.append(D)
