#Roll20_Simulator_python_ver1.1
#UPDATE
'''
Código para simular rolamento da dados aleatórios para uso em campanhas de RPG
Melhorias: 
Criar uma estrutura de classes e armas
Acertos, danos mais complexos e danos críticos
'''
from roll_dice import rolar_dado 

print("==========================================")
print(" FICHA DE PERSONAGEM: ")
print("==========================================")

print("\nEscolha a classe do personagem:")
print("1 - Mago")
print("2 - Guerreiro")
print("3 - Ranger")

classe = input("\nDigite a classe escolhida: ")

nome_ataque = "" #VAI SERVIR PARA ARMAZENAR QUAL ATAQUE ESCOLHIDO (ESPADA/MACHADO/BOLA DE FOGO/ ETC)
quantidade_dados = 0 #vai depender da arma escolhida - será atualziado após a escolha do personagem
lados_dado = 0 #muda de acordo com ataque
bonus_dano = 0 #vai mudar de acordo com o critico da arma
valor_minimo_acerto = 0 #usado para as comparações (se acerta ou se erra)
valor_minimo_critico = 0 #usado para comparação (se menor que valor definido para classe/arma critico, senao normal )
escolha_valida = True # "while true"

'''
SESSÃO DE COMPARAÇÕES DE CADA CLASSE::::
'''
match classe: #DEPENDENDO DA SUA ESCOLHA ENTRA EM CADA CATEGORIA: 
	case "1":
		nome_classe = "Mago"
		valor_minimo_acerto = 13 #SÓ ACERTA, SE O VALOR QUE O RAMDOM.RANDIT GERAR FOR MAIOR QUE 13
		valor_minimo_critico = 20 #SE O RANDOM.RANDIT GERAR == 20 (CRÍTICO)
		'''
		ESCOLHA DOS ATAQUES:::
		'''
		print("\nEscolha a magia:")
		print("1 - Bola de fogo, 8D6 de dano")
		print("2 - Relâmpago, 8D6 de dano")
		print("3 - Mísseis mágicos, 3D4 + 3 de dano")

		ataque_escolhido = input("\nDigite sua escolha: ")

		match ataque_escolhido:
			case "1":
				nome_ataque = "Bola de fogo"
				quantidade_dados = 8
				lados_dado = 6
				bonus_dano = 0
			case "2":
				nome_ataque = "Relâmpago"
				quantidade_dados = 8
				lados_dado = 6
				bonus_dano = 0
			case "3":
				nome_ataque = "Mísseis mágicos"
				quantidade_dados = 3
				lados_dado = 4
				bonus_dano = 3
			case _:
				print("\nMagia inválida.")
				escolha_valida = False #Fecha o "while true"
	case "2":
		nome_classe = "Guerreiro"
		valor_minimo_acerto = 9
		valor_minimo_critico = 17

		print("\nEscolha sua arma:")
		print("1 - Espada, 1D8 + 6 de dano")
		print("2 - Machado, 1D6 + 8 de dano")
		print("3 - Maça, 1D6 de dano")

		ataque_escolhido = input("\nDigite sua escolha: ")

		match ataque_escolhido:
			case "1":
				nome_ataque = "Espada"
				quantidade_dados = 1
				lados_dado = 8
				bonus_dano = 6
			case "2":
				nome_ataque = "Machado"
				quantidade_dados = 1
				lados_dado = 6
				bonus_dano = 8
			case "3":
				nome_ataque = "Maça"
				quantidade_dados = 1
				lados_dado = 6
				bonus_dano = 0
			case _:
				print("\nArma inválida.")
				escolha_valida = False #Fecha o "while true
	case "3":
		nome_classe = "Ranger"
		valor_minimo_acerto = 11
		valor_minimo_critico = 19

		print("\nEscolha sua arma:")
		print("1 - Arco longo, 1D6 de dano")
		print("2 - Besta, 1D8 de dano")
		print("3 - Adaga furtiva, 1D4 + 4 de dano")

		ataque_escolhido = input("\nDigite sua escolha: ")

		match ataque_escolhido:
			case "1":
				nome_ataque = "Arco longo"
				quantidade_dados = 1
				lados_dado = 6
				bonus_dano = 0
			case "2":
				nome_ataque = "Besta"
				quantidade_dados = 1
				lados_dado = 8
				bonus_dano = 0
			case "3":
				nome_ataque = "Adaga furtiva"
				quantidade_dados = 1
				lados_dado = 4
				bonus_dano = 4
			case _:
				print("\nArma inválida.")
				escolha_valida = False #Fecha o "while true
	case _:
		print("\nClasse inválida.")
		escolha_valida = False #Fecha o "while true


if escolha_valida:
	print("==========================================")
	print(" !!! INICIATIVA !!!")
	print("==========================================")
	input("\nPressione Enter para rolar o dado de ataque, D20...") #aguaradar o usuário interagir
	resultado_ataque = rolar_dado(20) #chama a função de rolar dados

	print("\n==========================================")
	print(f"Classe: {nome_classe}")
	print(f"Arma ou magia: {nome_ataque}")
	print(f"Resultado do D20: {resultado_ataque}")
	print("==========================================")
	if resultado_ataque < valor_minimo_acerto:
		print("\nO ataque errou!")
	else:
		print("\nO ataque acertou!")

	dano = rolar_dados(quantidade_dados, lados_dado, bonus_dano)

if resultado_ataque >= valor_minimo_critico:
	dano = dano * 2
	print("\nACERTO CRÍTICO!")
	print("O dano foi multiplicado por 2.")

print(f"\nDano total causado: {dano}")


