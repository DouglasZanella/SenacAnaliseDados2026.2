#CÓDIGOS DESENVOLVIDOS EM AULA

# for i in range(-10,10,1):
#     print(i)

#--------------------------------------------------------------------------------------------------
# WHILE::

# somador = int(input("Registro:"))
# controle = 0

# while controle <= 30:
#     controle=controle+somador
# somador = int(input("Registro:"))

# print("Oficina Lotada!")

# contador = 0 #lembrar que o "indice" 0 também contaria portanto ele repetirá 6 vezes;

# while contador < 5: #retirar o sinal de igual para que não repita uma 6° vez
#     print(f"Número {contador + 1} de 5:")
#     num = float(input("Digite um número: "))
#     dobro = num * 2
#     triplo = num * 3
#     quádruplo = num * 4
#     print(f" Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")

#     contador += 1
#--------------------------------------------------------------------------------------------------

# DO WHILE

print("--- Usando WHILE (Repetição Condicional) ---")
contador = 0 # Inicializamos o contador
limite = 5 # Definimos o limite

while True:
    if contador >= limite: # A condição de parada: Enquanto o contador for menor que 5
        break
    try:
        print(f"Número {contador + 1} de {limite}:")
        num = float(input("Digite um número: "))
        dobro = num * 2
        triplo = num * 3
        quádruplo = num * 4
        print(f" Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")
        contador = contador + 1 # IMPORTANTÍSSIMO! Incrementa o contador para evitar loop
        infinito
    except ValueError:
        print("Entrada inválida. Tente novamente.")
# Não incrementamos o contador para dar nova chance ao usuário  
