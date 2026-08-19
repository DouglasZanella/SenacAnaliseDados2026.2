'''
#codigo taxi_earning_python_Ver1.0 
Nome = input("Digite seu nome: ") 
Odo_inic = float(input("Digite o valor do Odônometro no início do dia:(em km): ")) 
Odo_final = float(input("Digite o valor do Odônometro no Final do dia:(em km):  ")) 
litros_gasto = float(input("\nDigite a quantidade de Litros de combustível consumidas: ")) 
saldo_bruto = float(input("\nDigite o quanto você recebeu dos passageiros no dia: ")) 
PRECO_COMBUSTIVEL = 6.15 


#calculo de Km/L: 

Km_percorrido = Odo_final - Odo_inic 

kml= (Km_percorrido / litros_gasto) 

#calculo de gasto por Km/L 
Gasto_combustivel = (litros_gasto * PRECO_COMBUSTIVEL) 

#Calcular Valor Líquido do dia: 
Saldo_liq = saldo_bruto - Gasto_combustivel 

print(f"\nOlá, {Nome}, Você percorreu {Km_percorrido} km") 
print(f"Seu consumo médio foi de {kml:.2f} km/L.") 
print(f"Seu gasto com combustível foi de R$ {Gasto_combustivel:.2f}.") 
print(f"Seu saldo líquido no dia foi de R$ {Saldo_liq:.2f}.") 
#---------------- AQUI ENCERRA O QUE FOI PEDIDO -------------------------  
'''

#codigo taxi_earning_python_Ver1.1 

nome = input("Digite seu nome: ") 
Odo_inic = float(input("Digite o valor do Odônometro no início do dia:(em km): ")) 
Odo_final = float(input("Digite o valor do Odônometro no Final do dia:(em km):  ")) 
litros_gasto = float(input("\nDigite a quantidade de Litros de combustível consumidas: ")) 
saldo_bruto = float(input("\nDigite o quanto você recebeu dos passageiros no dia: ")) 
PRECO_COMBUSTIVEL = 6.15 

 #verifica se a quantidade de litros é maior que 0 (para não haver erro de divisão por 0) 

if litros_gasto > 0:
    Km_percorrido = Odo_final - Odo_inic
    kml= (Km_percorrido / litros_gasto)
    Consumo_medio = (litros_gasto * PRECO_COMBUSTIVEL)
    saldo_liq = saldo_bruto - Consumo_medio 
    print(f"\nOlá, {nome}, Você percorreu {Km_percorrido} km") 
    print(f"Seu consumo médio foi de {kml:.2f} km/L.") 
    print(f"Seu gasto com combustível foi de R$ {Consumo_medio:.2f}.") 
    print(f"Seu saldo líquido no dia foi de R$ {saldo_liq:.2f}.") 
else:
    print("\no valor de litros gasto precisa ser maior do que 0(zero)") 