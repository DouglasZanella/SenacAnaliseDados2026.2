# #CÓDIGOS REALIZADOS NA AULA
# #----------- LISTAS ------------ 
# # impares = []
# # print (type(impares))
# # impares = [3,5,13,27]
# # print(impares[0])
# # print(type(impares[0]))
# # print(impares[0])
# # print(impares[-2])#negativo dentro dos colchetes começa a contagem da lista pela direita

# # lista_01 = [
# #     12,
# #     "Pedro",
# #     12.53343,
# #     "}{~]~[~]{}]",
# #     False,
# #     0,
# #     [2,4,6,8]
# #     ]#para pular linha em python não precisa usar SHIFT para pular linha, pode ser pulando apenas com "ENTER"

# # print(lista_01[1],lista_01[2],lista_01[4])
# # print(lista_01[6][2]) #dessa forma eu consigo acessar uma lista dentro de outra, pois cada "colchetes" seria o proximo elemento encapsulado

# #LISTAS COM CONDICIONAIS::

# lista_02 = ["Márcia"]

# # if "Márcia" in lista_02:
# #     print(Está presente)
# # else:
# #     print("Não está prsente")

# #LSITAS COM LOOPING :: 

# participantes = ["Zé", "José", "Josefa", "Josinaldo", "José João"]

# for participante in participantes:
#     print (participante)
# print("----------------------------")

# for nome in participantes:
#     if nome == "Josefa":
#         print("\nTESTE DE IF ::::\n")
#         print(nome,"\n")
# print("----------------------------")
    
# #ADICIONANDO ITENS NA LISTA    
# partic_2 = "Josiel"
# participantes.append(partic_2)#append adiciona um elemento no final da lista
# participantes.insert(0,partic_2)#insert adiciona um elemento aonde eu indico (a indicação vem antes (antes da virgula))
# #OBSERVAÇÃO: O ÚLTIMO ÍNDICE DE UMA LISTA PODE SER LIDO COMO -1 

# print("LISTA ATUALIZADA - ADIÇÃO \n")
# print(participantes, "\n")
# print("----------------------------")

# #REMOVENDO ITENS DA LISTA::
# participantes.append("Josefa")#adiciona outro item JOSEFA ao final da lista
# print(participantes, "\n")
# participantes.pop(1)
# participantes.remove("Josefa")#remove a primeira identificação do item na lista (inicio)
# print("LISTA ATUALIZADA - REMOÇÃO\n")
# print(participantes, "\n")
# print("----------------------------")

# #OUTRAS FUNÇÕES DA LISTA::
# participantes.reverse()
# participantes.append("Josefa")

# print("LISTA ATUALIZADA - FUNÇÕES DA LSITA\n")
# print(participantes, "\n")
# print("----------------------------")

#UTILIZANDO TUPLAS 

# participantes = ("Isaque", "Luana", "Fernando", "Bianca", "Ana Paula")+("Hugo")
# # print(participantes)
# partic_2 =("Fernando", "111.111.*********", "Av. Dr. Tibúrcio 444", "DDD2199999-9999")#TUPLAS são imutáveis e funcionam para proteger os dados 
# print(partic_2.count("Fernando"))

# print(participantes, type(participantes))

#UTILIZANDO SETS::

# numeros_pares = {
#     202,
#     203,
#     204,
#     204,
#     205,
#     219,
#     291,
#     292,
#     202,

# }

# print(numeros_pares, type(numeros_pares))

# numeros_impares = {
#     111,111,112,291,291,205
# }
# print(numeros_pares.intersection(numeros_impares))
# numeros_pares.remove(205 and 291) 
# print(numeros_pares)

#UTILIZANDO DICIONÁRIOS :: 

produtos = {"nome":"Maçã", "preco":5.99,"regiao":"Sudeste"}
print(produtos, (type(produtos)))
print(produtos.items())
print(produtos.keys())
print(produtos.values())
print(produtos.get("preco"))
produto_novo = produtos.copy()
print("--------------CÓPIA------------")
print(produto_novo)
produto_novo["preco"]=7.99
print("NOVO DICIONARIO:")
print("\n",produto_novo)
###
achadinhos = {} #o python considera qualquer abertura de chaves como dicionario e nao set 
print(achadinhos, type(achadinhos))
achadinhos["capinha celular"]=12.99
print(achadinhos)