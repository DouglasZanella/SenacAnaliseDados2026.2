nome = input("Digite seu nome: ") 
idade = int(input("Digite sua idade: ")) 
resp1 = input("Você possui CNH? (sim ou nao): ") 
resp2 = input("Você Bebeu hoje? (sim ou nao): ") 

# if idade < 18: 
#     print(f"Olá {nome}, você não está apto a dirigir (Menor de idade).") 
# else: 
#     if resp1 == "nao": 
#         print(f"Olá {nome}, você não está apto a dirigir (Não possui CNH).") 
#     else: 
#         if resp2 == "sim": 
#             print(f"Olá {nome}, você não está apto a dirigir (Bebeu hoje).") 
#         else: 
#             print(f"Parabéns {nome}, você está apto a dirigir!") 

#USANDO A VERSÃO ELIF:
if idade < 18: 
    print(f"{nome}, Vai de Uber tu é Menor") 
elif resp1 == "nao": 
    print(f"{nome}, Vai de Uber até ter uma habilitação.") 
elif resp2 == "sim": 
    print(f"{nome},Ta maluco? vai de Uber") 
else: 
    print(f"Boa {nome}!, vai lá") 

'''
#OUTRA FORMA DE FAZER: MELHORANDO A SINTAXE

if idade >= 18 and resp1 == "sim" and resp2 == "nao":  

print("Você está apto a dirigir!") 

else:  

print("Você NÃO está apto a dirigir.")            
'''