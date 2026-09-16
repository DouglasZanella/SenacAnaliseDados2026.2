#Roll20_Simulator_python_ver1.0
#versão simples do exercicio
'''
Código para simular rolamento da dados aleatórios para uso em campanhas de RPG
'''

from roll_dice import rolar_dado

print("====================================")
print(" SIMULADOR DE BATALHA")
print("====================================")


input("\nPressione Enter para rolar o Ataque (d20)...")

resultado_ataque = rolar_dado(20) #teste de ataque é um D20

input("\nPressione Enter para rolar o Dano (d8)...") #d8 é o dano da arma
resultado_dano = rolar_dado(8)


print("\n====================================")
print(" RESULTADO DA BATALHA")
print("====================================")

print(f"Resultado do ataque (d20): {resultado_ataque}")
print(f"Resultado do dano (d8): {resultado_dano}")
print("====================================")
