#CÓDIGOS DESENVOLVIDOS EM AULA 

import pandas as pd # alias 'pd'
import numpy as np # alias 'np'
import openpyxl
'''
Sempre que for usado o "as" seguido de um nome, é como se fosse 
atribuido o nome inteiro da biblioteca a um "apelido" para facilitar 
o uso: import pandas "como" pd. 
Esse processo chama-se ALIAS
'''

# numeros_impares= [43, 55, 1, 3, 11, 27, 109]
# numeros_seq = [2,3,4,5,6,6,7]
# print(type(numeros_impares))
# # matriz_numero = numeros_impares + numeros_seq#testes realizados 

# # matriz_numero = pd.series(matriz_numero)#testes realizados
# serie_impares = pd.Series(numeros_impares)#aqui a lista de nº impares foi "transformada" em uma matriz da biblioteca Python.
# print(serie_impares)
# print(type(serie_impares))
# print("======================================")
# print(serie_impares[4]) #"- traz a linha 4 especificamente")#uma série identifica os valores a partir da linha e não mais do índice, por isso não posso trazer números negativos;
# print("======================================")
# print(serie_impares.sum())# traz a soma de todos os elemtnso da lista")
# print("======================================")
# print(serie_impares.mean())#- traz a média de todos os elemtnso da lista
# print("======================================")
# print(serie_impares.min())#-traz o valor minimo (maior) de todos os elemtnso da lista
# print("======================================")
# print(serie_impares.max())#- traz o valor maximo (maior) de todos os elemtnso da lista
# print("======================================")
# print(len(serie_impares))#- traz tamanho da lista
# print("======================================")
# print(serie_impares.describe())#- traz a descrição  de todos os elementos da lista
# print("======================================")
# print(serie_impares[serie_impares>50])#- 
# print("======================================")

# serie2_impares = pd.Series(
#     numeros_impares,
#     index = ['a','b','c','d','e','f','g'])
    
# print(serie2_impares)

#INICIA AQUI A AULA 12(09/09/2026)

# filmes = {
#     'título': ["Lagoa Azul", "Agente Secreto", "Gênio indomável"],
#     'Categoria': ["Romance", "Ação", "Drama"],
#     'ano': ["1980", "2025", "1997"]
# }

# tabela_filmes = pd.DataFrame(filmes)

# print(filmes)
# print(type(filmes))
# print(tabela_filmes)
# print(type(tabela_filmes))


# print(serie_impares)
# print("\n==========DEPOIS==============\n")

# quadrado_serie_impares = serie_impares*serie_impares
# print(quadrado_serie_impares)

# == ========= LEITURA DE ARQUIVOS XLS =========== == 

#Variável          #Comando    #Caminho do arquivo  #argumentos de leitura
leitura_invest = pd.read_excel("base_invest.xlsx", sheet_name=2)
print(leitura_invest)