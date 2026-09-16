'''
FUNÇÃO SECUNDÁRIA PARA ROLAR DADOS ALEATÓRIOS
SERÁ UTILIZADA PELA UFNÇÃO PRINCIPAL 
'''

import random #importar a biblioteca Random (aleatorio)

def rolar_dado(lados): #função de rolar dados, recebe o parâmetro de "lados" possíveis
	resultado = random.randint(1, lados) #minimo, máximo
	return resultado