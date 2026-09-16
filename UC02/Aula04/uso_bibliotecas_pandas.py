#CÓDIGOS PDF AULA 2

#lOC -> localiza elementos com dados qualitativos
#ILOC -> localiza elementos com base no indice
#QUERY ->

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# filmes = {
#     'título': ["Lagoa Azul", "Agente Secreto", "Gênio indomável", "A freira","Brinquedo Assassino","Top Gun"],
#     'Gêreno': ["Romance", "Ação", "Drama", "Terror","Terror","Aventura"],
#     'ano': ["1980", "2025", "1997", "2022","1995","1986"],
#     'Faturamento':[6.5, 4, 5.5, 3, 9, 7.3]
# }

# indices = ['Filme1', 'Filme2', 'Filme3','Filme4','Filme5','Filme6' ]

# tabela_filmes = pd.DataFrame(filmes, index=indices)
# print(tabela_filmes)

# # print("="*40)
# # print(tabela_filmes.iloc[0])

# # print("="*40)
# # print(tabela_filmes.iloc[1])

# # print("="*40)
# # print(tabela_filmes.iloc[-1])

# # print("="*20, "LOC", "="*20)
# # print(tabela_filmes.loc['Filme5'])

# # print("="*20, "LOC intervalos", "="*20)
# # print(tabela_filmes.loc['Filme3': 'Filme5'])

# # print("="*20, "ILOC - intervalos ", "="*20)
# # print(tabela_filmes.iloc[3:5])

# print("="*20, " QUERY ", "="*20)
# consulta1 = tabela_filmes.query("Faturamento > 6")
# print(consulta1)
# # < > <= => == != and or not in 

# CONTINUAÇÃO DOS CÓDIGOS NA AULA 14(14/09/2026) 

# dados = np.array([12,15,17, 20, 22, 25, 28, 30, 35, 40,55, 60, 68, 72, 84, 88, 91, 100])
# print(dados)

# # CALCULAR QUARTIS
# q1 = np.percentile(dados, 25) # o 1° Quartil representa 25% dos dados
# q2 = np.percentile(dados, 50) # A Mediana é a representalção de 50% dos dados
# q3 = np.percentile(dados, 75) # o 3° Quartil representa 75% dos dados

# # EXIBIR OS RESULTADOS
# print(f"\nPrimeiro Quartil(Q1): {q1}")
# print(f"\nSegundo Quartil(Q2): {q2}")
# print(f"\nTerceiro Quartil(Q3): {q3}")

df_transacoes = pd.read_excel('base_invest.xlsx', sheet_name="Transacoes")

#mostra as 5 primeira linhas de uma amostra
print(df_transacoes.head())
print("="*30)


#mostra as 5 ultimas linhas de uma amostra
print(df_transacoes.tail())
print("="*30)

#          dataframe|  [nome da couna aanlisada] quantile = percentile (muda devido a biblioteca ser diferente)
q1_preco = df_transacoes['preco'].quantile(0.25)
q2_preco = df_transacoes['preco'].quantile(0.50)
q3_preco = df_transacoes['preco'].quantile(0.75)

print(f"Preço Q1: {q1_preco}") 
print(f"Preço Q2: {q2_preco}") 
print(f"Preço Q3: {q3_preco}")
print("="*30, "\n")

contagem_operacao = df_transacoes['operacao'].value_counts()

#criar i, gráfico de barras
contagem_operacao.plot(kind='barh', title='Tipos de Operação')

#Mostrar gráfico:
plt.show()
