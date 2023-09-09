#13. Funções - 

"""print()
input()
len()
max()"""

#Criação de Funções 

#Função inicial

"""def saudacao(): 
    print("Seja bem vindo")
    print("É um prazer te-lo como aluno")


saudacao()
saudacao()
saudacao()"""

#Função com paramentros

"""def saudacao(nome, curso): 
    print(f"Seja bem vindo, {nome}")
    print(f"É um prazer te-lo como aluno de {curso}")

saudacao("Camile", "Python")
saudacao("Aline", "Java")
"""

#função com paramentros default

def saudacao(nome, curso="Python"): 
    print(f"Seja bem vindo, {nome}")
    print(f"É um prazer te-lo como aluno de {curso}")

saudacao("Camile")

#Funções com retorno

def soma(num1, num2):
    return num1 + num2

resultado = soma(5,7)
print("O resultado da soma")
