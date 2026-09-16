'''
FUNÇÃO SECUNDÁRIA PARA ROLAR DADOS ALEATÓRIOS
SERÁ UTILIZADA PELA UFNÇÃO PRINCIPAL 
'''

import random #importar a biblioteca Random (aleatorio)

def rolar_dado(quantidade, lados, bonus=0):
	'''
	rola os dados definindo a quantidade de vezes e a quantidade de lados, por xemplo: 
	rola 8D6 = 8 vezes (FOR repete 8) um dado com minimo de 1 e máximo de 6
	'''
	dano_total = 0 #Salva o valor de dano toal acumulado adquirido nos dados
	for i in range(quantidade):#para cada vez que a quantiadde de dados for definida faça:
		resultado_dado = random.randint(1, lados)#o resultado do dado vai ser no minimo 1 e no maximo o numero de lado do dado definido e passado como parâmetro
		dano_total += resultado_dado #armazena o valor aleatório no dano

	dano_total += bonus #caso haja bonus de arma/força/magia ele será recebido pela função e salvo depois somado. 

	return dano_total