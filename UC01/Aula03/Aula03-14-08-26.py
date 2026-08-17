#CÓDIGOS DESENVOLVIDOS DURANTE A AULA 
'''
nome = "Maria" #Str
idade = "30" #int
preco = 19.90 #float
esta_matricula = True #bool
notas = [8.0, 7.5] #list
aluno = ("Maria", 30) #tupla
disciplina = {"Python", "Lógica"} #set
cadastro = {"nome": "Maria", "idade": 30} #dict

print(type(nome))
print(type(idade))
print(type(preco))
'''

# x = 15
# y = 20

# print("x é maior que y?", x > y)
# print("x é igual a y?", x == y)

# POsso armazenar um booleano dentro de veriáveis

# resposta = x>y
# print(resposta)
# print(type(resposta))
'''
tem_carteira = True
idade = 18
tem_carro = False
pode_dirigir = idade >= 18 and tem_carteira
print("Pode dirigir?", pode_dirigir)
print("Pode dirigir e tem carro?", pode_dirigir and tem_carro)
'''
'''
resposta = input("voce bebeu?(sim/nao\n")

if resposta == "sim":
    print("pede uber")
else:
    if resposta =="nao":
        print("vai lá chefia!")
    else:
        print("Digitou errado")
'''
'''
#Ideia desenvolvida para teste do OPERADOR AND
resp1 = input("voce tem cnh?(sim/nao\n")
resp2 = input("voce bebeu?(sim/nao\n")

if resp1 == "sim" and resp2 == "nao": 
    print("vai la chefia")
else:
    if  resp1 == "sim" and resp2 == "sim": 
        print("Pede uber")
    else:
        if resp1 == "nao" and resp2 == "sim": 
            print("Pede Uber")
        else:
            if resp1 == "nao" and resp2 == "nao": 
                print ("pede uber")
            else: 
                print("digitou errado")
'''
'''
#Ideia desenvolvida para teste estrutura ELIF
resp1 = input("voce tem cnh?(sim/nao\n")
resp2 = input("voce bebeu?(sim/nao\n")

if resp1 == "sim" and resp2 == "nao": 
    print("vai la chefia")
elif resp1 == "sim" and resp2 == "sim": #LEMBRAR SEMPRE DA IDENTAÇÃO CORRETA 
    print("Pede uber")
elif resp1 == "nao" and resp2 == "sim": 
    print("Pede Uber")
elif resp1 == "nao" and resp2 == "nao": 
    print ("pede uber")
else: 
    print("digitou errado")
'''

locomocao = input("Qual sua locomocao?")
choveu = True

if choveu and locomocao == "moto":
    resultado = "molhou"
elif not choveu and locomocao =="moto":
    resultado = "To Seco"
else:
    resultado = "Ta seco"

print(f"nesse caso então {resultado}")