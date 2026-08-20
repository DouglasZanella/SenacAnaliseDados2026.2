'''
#codigo origem_produto_python_Ver1.0 
cod_prod = int(input("Digite o código do produto (de 1 a 11): "))

#verifica o codigo do produto:  
match cod_prod:
    case 1:
        print("O produto pertence a região: SUL")
    case 2:
        print("O produto pertence a região: NORTE") 
    case 3:
        print("O produto pertence a região: LESTE") 
    case 4:
        print("O produto pertence a região: OESTE") 
    case 5 | 6: #em python quando utilizar match, não preciso do operador lógico OR, mas sim "|" 
        print("O produto pertence a região: NORDESTE") 
    case 7 | 8 | 9:
        print("O produto pertence a região: SUDESTE") 
    case 10:
        print("O produto pertence a região: CENTRO-OESTE") 
    case 11:
        print("O produto pertence a região: NOROESTE") 
    case _:
        print(f"Você Digitou: {cod_prod}, esse produto é importado") 
#---------------- AQUI ENCERRA O QUE FOI PEDIDO -------------------------  
'''
#codigo origem_produto_python_Ver1.1 
cod_prod = int(input("Digite o código do produto (de 1 a 11): "))

match cod_prod: #POSSO DEFINIR VARIAVEL DENTRO DA ESTRUTURA 
    case 1:
        regiao = "SUL"
    case 2:
        regiao = "NORTE"
    case 3:
        regiao = "LESTE"
    case 4:
        regiao = "OESTE"
    case 5 | 6:
        regiao = "NORDESTE"
    case 7 | 8 | 9:
        regiao = "SUDESTE"
    case 10:
        regiao = "CENTRO-OESTE"
    case 11:
        regiao = "NOROESTE"
    case _:
        regiao = "IMPORTADO"  
        
print(f"O produto é da região: {regiao}") 