#função consultar_pedido_python_ver1.0()

'''
para funcionar vou precisar importar funções externas, por exemplo: 
from adicionar_pedido import adicionar_pedido
from remover_pedido import remover_pedido
from cancelar_pedido import cancelar_pedido
'''

#criação de uma lista "falsa" para testes:::::
lista_pedidos = [
    {
        "numero_pedido": 20,
        "mesa": 4,
        "status": "PREPARANDO",
        "pagamento": "PENDENTE",
        "garcom": "José",
        "valor_total": 105.98
    },
    {
        "numero_pedido": 21,
        "mesa": 7,
        "status": "PRONTO",
        "pagamento": "PENDENTE",
        "garcom": "Cleiton",
        "valor_total": 75.90
    }
]


# Funções para testes
def remover_item(pedido):
    print(
        f"\nUm item seria removido do "
        f"pedido nº {pedido['numero_pedido']}."
    )


def adicionar_item(pedido):
    print(
        f"\nUm item seria adicionado ao "
        f"pedido nº {pedido['numero_pedido']}."
    )


def cancelar_pedido(pedido):
    pedido["status"] = "CANCELADO"

    print(
        f"\nO pedido nº {pedido['numero_pedido']} "
        "foi cancelado."
    )
#--------------------------------------FIM DO BLOCO DE TESTES --------------------------------------------------

# def mostra_tela(pedido):
#       print( 
#       "\n==============================================="
#        "\n| SEU PEDIDO |"
#        "\n==============================================="
#     )
#         print(f"Número: {pedido['numero_pedido']}") 
#         print(f"Mesa: {pedido['mesa']}") 
#         print(f"Garçom: {pedido['garcom']}") 
#         print(f"Status: {pedido['status']}") 
#         print(f"Pagamento: {pedido['pagamento']}") 
#         print(f"Total: R$ {pedido['valor_total']:.2f}")    
#         

def consultar_pedidos(numero_digitado, lista_pedidos):  
    '''
    Função que procura o pedido dentro da lista de pedido
           (essa lista pode ter sido criada quando a função "criar_pedido()" é executada, 
           esta função recebe o nº digitado e a lista criada como parâmetros 
           se encontrar a lista vazia, retornará "nada", se não encontrar o valor,
           retornará que o pedido não existe, se encontrar um pedido equivalente ao número registrado,
           retornará o pedido
    '''
    consulta = "s"
    try:
        while consulta == "s":
            numero_digitado = int(input("Digite o número do pedido que deseja consultar: ")) 
            if len(lista_pedidos) == 0:
                return None

            for pedido in lista_pedidos:
                if pedido["numero_pedido"] == numero_digitado: 
                    return pedido 
                consulta = input("Desejo continuar a consulta? (s/n)\n")
            return None
    except ValueError:
        print("Entrada inválida. Digite somente números.") 
        return None
    
        
    


# # TESTE PARA VER SE A FUNÇÃO ESTÁ RETORTANDO CORRETAMENTE:::::: 
# while True :  
#     pedido = consultar_pedidos()
#     if pedido != None: 
#         print("\n========== DADOS DO PEDIDO ==========") 
#         print(f"Número: {pedido['numero_pedido']}") 
#         print(f"Mesa: {pedido['mesa']}") 
#         print(f"Garçom: {pedido['garcom']}") 
#         print(f"Status: {pedido['status']}") 
#         print(f"Pagamento: {pedido['pagamento']}") 
#         print(f"Total: R$ {pedido['valor_total']:.2f}")
        
# print("\n=========================================") 
# print("\nTecle 1 para: Adicionar mais itens"
# "\nTecle 2 para: Remover Itens"
# "\nTecle 3 para: Continuar com o Pedido atual"
# "\nTecle 4 para: Cancelar o Pedido"
# )  

# print("\n=========================================\n")
# resp = input("Com odeseja prosseguir? -> TECLE 1 | 2 | 3 | 4")
# try:
#     match resp:
#         case 1:
#             adicionar_pedido(resp)
#         case 2:
#             remover_pedido(resp)
#         case 3:
#             cancelar_pedido(resp)
#         case _:
#             print("Entrada inválida")
# except ValueError:
#     print("Entada inválida, digite novamente")

pedido_encontrado = None #aqui o pedido inicia vazio, só passará a ter valor quando a função for executado no while
continuar_consulta = "s" #define o valor para o while iniciar o loop 

while continuar_consulta == "s":
    try:
        numero_digitado = int(input("\nDigite o número do pedido que deseja consultar: "))
        pedido_encontrado = consultar_pedidos(numero_digitado,lista_pedidos)

        if pedido_encontrado is None: #se não tiver nada na lista ou não encontrar o nº de pedido, ele ainda vai estar como None
            print(
                f"\nO pedido nº {numero_digitado} não foi encontrado.")
        else:
            mostrar_pedido(pedido_encontrado)#se achar, ele puxa lá da variável que armazenou a execução da função com o numero_digitado

        continuar_consulta = input("\nDeseja realizar outra consulta? (s/n): \n").lower()#lower para colocar em minusculo

        while continuar_consulta != "s" and continuar_consulta != "n": #valida se foi digitado s ou n
            print("\nResposta inválida.")

            continuar_consulta = input("Digite apenas s ou n: ").lower()

    except ValueError:
        print(
            "\nEntrada inválida. O número do pedido deve conter somente números.")


# Verifica se existe um pedido para poder dar opções ao usuário
if pedido_encontrado != None: 
    print("\n=========================================")
    print("Tecle 1 para: Adicionar mais itens")
    print("Tecle 2 para: Remover itens")
    print("Tecle 3 para: Continuar com o pedido atual")
    print("Tecle 4 para: Cancelar o pedido")
    print("Tecle 0 para: Sair")
    print("=========================================")

    opcao = input("\nComo deseja prosseguir? ") #salva a resposto em opcao

    match opcao: #aqui entra a ligação com as demais funções::
        case "1":
            adicionar_item(pedido_encontrado)
        case "2":
            remover_item(pedido_encontrado)
        case "3":
            print(f"\nO pedido nº {pedido_encontrado['numero_pedido']} continuará sem alterações." )
        case "4":
            cancelar_pedido(pedido_encontrado)
        case "0":
            print("\nSaindo da consulta")
        case _:
            print("\nOpção inválida.")
else: #se naõ tem um pedido diferente de None significa que não tem pedidos com essa numeração a variavel Pedido_enconrtado ainda possui valor "vazio"
    print("\nPedido Inexistente")