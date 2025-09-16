# Importar a biblioteca drive do módulo google.colab
from google.colab import drive

# Monte o Google Drive
drive.mount('/content/drive')

# Instalar uma biblioteca
# !pip install name

# Instalar uma versão específica
# !pip install name==1.2.0

# Instalar múltiplas bibliotecas
# !pip install name1 name2 

# Exemplos de números de ponto flutuante
numero1 = 3.14

numero2 = -2.71
numero3 = 0.5

# Exemplos de operações com números de ponto flutuante
soma = numero1 + numero2
subtracao = numero1 - numero3
multiplicacao = numero2 * numero3
divisao = numero1 / numero3
potencia = numero1 ** 2

resultado = 0.1 + 0.2
print(resultado) # O resultado será 0.30000000000000004 

# Conversão para int
numero_inteiro = int(numero1)
# Conversão para str

numero_str = str(numero2) 

# Funções matemáticas básicas
numeros = [1.5, 2.3, 0.8, -2.0]
valor_absoluto = abs(numero2)
maior_numero = max(numeros)
soma_total = sum(numeros)
media = sum(numeros) / len(numeros)

# Exemplos de operações com números inteiros
numeros = [1.5, 2.3, 0.8, -2.0]
valor_absoluto = abs(numero2)
maior_numero = max(numeros)
soma_total = sum(numeros)

# Exemplos de operações com strings
nome = "João"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome # Concatenação
mensagem_repetida = "Olá! " * 3 # Repetição
parte_do_nome = nome[0:2] # Fatiamento (slicing)

# Exemplos de funções e métodos para strings
texto = "Olá, mundo!"
tamanho = len(texto) # Retorna o tamanho da string
maiusculo = texto.upper() # Converte para letras maiúsculas
minusculo = texto.lower() # Converte para letras minúsculas
contagem = texto.count('o') # Conta a ocorrência de um caracter ou substring
substituida = texto.replace('mundo', 'Python') # Substitui parte da string por outra

# Exemplos de operações com valores booleanos
valor1 = True
valor2 = False
resultado_and = valor1 and valor2
resultado_or = valor1 or valor2
resultado_not = not valor1 

# Exemplo de expressão condicional
idade = 18
if idade >= 18:
   print("Você é maior de idade.")
else:
   print("Você é menor de idade.")

# Exemplos de operadores de comparação
# ==: igual a
# !=: diferente de
# <: menor que
# >: maior que
# <=: menor ou igual a
# >=: maior ou igual a

# Exemplo de expressão condicional
idade = 18
if idade >= 18:
   print("Você é maior de idade.")
else:
   print("Você é menor de idade.") 

# Exemplo de expressão condicional
idade = 18
if idade >= 18:
   print("Você é maior de idade.")
else:
   print("Você é menor de idade.") 

# Exemplo de acesso a elementos em uma lista
numeros = [10, 20, 30, 40, 50]
primeiro_elemento = numeros[0] # 10
segundo_elemento = numeros[1] # 20
ultimo_elemento = numeros[-1] # 50 (último elemento da lista)

# Exemplo de modificação de elementos em uma lista
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
# Adição de elementos
lista_a.append(4) # [1, 2, 3, 4]
lista_b.insert(0, 0) # [0, 4, 5, 6]
# Remoção de elementos
lista_a.remove(2) # [1, 3]
elemento_removido = lista_b.pop(2) # elemento_removido = 5, lista_b = [0,4, 6]
# Concatenação de listas
lista_concatenada = lista_a + lista_b # [1, 3, 0, 4, 6]
# Fatiamento (slicing)
sublista = lista_concatenada[1:4] # [3, 0, 4]

# Exemplos de funções úteis para listas
numeros = [5, 2, 8, 1, 9]
tamanho = len(numeros) # Retorna o tamanho da lista (5)
maior = max(numeros) # Retorna o maior valor (9)
menor = min(numeros) # Retorna o menor valor (1)
soma_total = sum(numeros) # Retorna a soma dos elementos (25)

# Exemplos de tuplas
tupla_numeros = (1, 2, 3, 4, 5)
tupla_frutas = ('maçã', 'banana', 'laranja')
tupla_mista = (10, 'python', True)

# Exemplo de acesso a elementos em uma tupla
numeros = (10, 20, 30, 40, 50)
primeiro_elemento = numeros[0] # 10
segundo_elemento = numeros[1] # 20
ultimo_elemento = numeros[-1] # 50 (último elemento da tupla)

# Exemplos de operações com tuplas
tupla_numeros = (1, 2, 3, 4, 5)
tupla_frutas = ('maçã', 'banana', 'laranja')
tupla_mista = (10, 'python', True)

# Exemplo de acesso a elementos em uma tupla
tupla_a = (1, 2, 3) , tupla_b = (4, 5, 6)

# Concatenação de tuplas
tupla_concatenada = tupla_a + tupla_b # (1, 2, 3, 4, 5, 6)
# Repetição de tupla
tupla_repetida = tupla_a * 3 # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Exemplos de dicionários
dicionario_pessoas = {
    'nome': 'João',
    'idade': 30,
    'cidade': 'São Paulo'
}
dicionario_notas = {
    'Matemática': 9.5,
    'Ciências': 8.0,
    'História': 7.5
}

# Exemplo de acesso a elementos em um dicionário
pessoa = {
   'nome': 'Maria',
   'idade': 25,
   'cidade': 'Rio de Janeiro'
}
nome = pessoa['nome'] # 'Maria'idade = pessoa['idade'] # 25
cidade = pessoa['cidade'] # 'Rio de Janeiro'

# Exemplo de acesso a elementos em um dicionário
pessoa = {
   'nome': 'Maria',
   'idade': 25,
   'cidade': 'Rio de Janeiro'
}
nome = pessoa['nome'] # 'Maria'idade = pessoa['idade'] # 25
cidade = pessoa['cidade'] # 'Rio de Janeiro'

# Exemplos de funções úteis para dicionários
pessoa = {'nome': 'João','idade': 30,'cidade': 'São Paulo'}

tamanho = len(pessoa) # Retorna o número de pares chave-valor (3)

chaves = pessoa.keys() # Retorna as chaves do dicionário ('nome', 'idade', 'cidade')

valores = pessoa.values() # Retorna os valores do dicionário ('João', 30, 'São Paulo')

pares = pessoa.items() # Retorna uma lista de tuplas com os pares chave-valor

# Acessando elementos em uma matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
elemento = matriz[1][2] # Acessando o elemento na segunda linha e terceira coluna (6)

# Exemplo de uso do NumPy para trabalhar com matrizes

import numpy as np

# Criando matrizes usando NumPy

matriz_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

matriz_b = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Adição de matrizes

soma = matriz_a + matriz_b

# Multiplicação por um escalar

escalar = 2

resultado = escalar * matriz_a

# Multiplicação de matrizes

produto = np.dot(matriz_a, matriz_b)

# Transposição de matriz

transposta = matriz_a.T

# Exemplo 1: Conversão de um valor numérico para inteiro
valor_float = 3.14
inteiro = int(valor_float) # Resultado: 3
# Exemplo 2: Conversão de uma string para inteiro
valor_string = "42"
inteiro = int(valor_string) # Resultado: 42 

# Exemplo 1: Conversão de uma string para lista de caracteres
texto = "Python"
lista_caracteres = list(texto) # Resultado: ['P', 'y', 't', 'h', 'o', 'n']
# Exemplo 2: Conversão de uma tupla para lista
tupla = (1, 2, 3)
lista = list(tupla) # Resultado: [1, 2, 3] 

# Exemplo de TypeError

numero = 5
texto = "Python"
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
resultado = numero + texto 

# Exemplo de ValueError
texto = "Python"
# ValueError: invalid literal for int() with base 10: 'Python' 
numero = int(texto)

# Exemplo de TypeError
numero = 42
texto = "42"
# TypeError: '<' not supported between instances of 'int' and 'str'
resultado = numero < texto

# Exemplo de IndexError
# try:    
#     # code to run
# except:    
#     # handle error

# adição
a = 5
b = 3
resultado = a + b # Resultado: 8

# adição
a = 5
b = 3
resultado = a + b # Resultado: 8

# multiplicação
a = 3
b = 4
resultado = a * b # Resultado: 12

# divisão
a = 10
b = 3
resultado = a / b # Resultado: 3.3333333333333335

# divisão inteira
a = 10
b = 3
resultado = a // b # Resultado: 3

# resto da divisão
a = 10
b = 3
resto = a % b # Resultado: 1

# potência
a = 2
b = 3
resultado = a ** b # Resultado: 8

# precedência dos operadores
resultado = 2 + 3 * 4 # Resultado: 14 (multiplicação antes da adição)

resultado = (2 + 3) * 4 # Resultado: 20 (parênteses para alterar a ordem)

# Igual (==)
a = 5
b = 5
resultado = a == b # Resultado: True

# Diferente (!=)
a = 10
b = 7
resultado = a != b # Resultado: True

# menor que (<)
a = 5
b = 8
resultado = a < b # Resultado: True

# maior que (>)
a = 10
b = 7
resultado = a > b # Resultado: True

# menor ou igual (<=)
a = 10
b = 15
resultado = a <= b # Resultado: True

# maior ou igual (>=)
a = 5
b = 5
resultado = a >= b # Resultado: True

# loop for
sequencia = [1, 2, 3, 4, 5]
for elemento in sequencia:    
    # Código a ser executado para cada elemento

# Exemplo de loop "for" com listas
    frutas = ['maçã', 'banana', 'laranja']

for fruta in frutas:   
    print(fruta)

# Exemplo de loop "for" com string
texto = 'Python' 
for letra in texto:
    print(letra)

# Exemplo de loop "for" com intervalo numérico
for numero in range(1, 6):    
    print(numero)

# Exemplo de loop "while"
condition = True
while condition:    
      # Código a ser executado enquanto a condição for verdadeira

# Exemplo de loop "while"
    contador = 0
while contador < 5:    
    print(contador)
    contador += 1

# Exemplo de loop "while" com "break"
contador = 0
while True:    
    print(contador)    
    contador += 1    
    if contador >= 5:        
        break

# Exemplo de loop "while" com "continue"
contador = 0
while contador < 5:    
    contador += 1    
    if contador == 3:        
        continue # Pula a iteração quando contador == 3
    print(contador)

# Gera uma lista de números de 5 a 10
lista = list(range(5, 11))
print(lista)# Saída: [5, 6, 7, 8, 9, 10]
