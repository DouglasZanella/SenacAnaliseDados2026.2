# função consultar_pedido_python_ver1.3()
# foram feitos melhorias nessa versão

'''
#para funcionar vou precisar importar funções externas, por exemplo:
from adicionar_item_pedido import adicionar_item_pedido
from remover_pedido import remover_pedido
from cancelar_pedido import cancelar_pedido
'''
# criação de uma lista "falsa" para testes:::::
# ----------------------------------------------BLOCO DE TESTES------------------------------------
pedidos = [
    {
        "numero_pedido": 1,
        "numero_da_mesa": 2,
        "itens": "Sushi",
        "quantidade": 8,
        "status": "ABERTO",
        "garcom": "Carlos",
        "observacoes": "Sem wasabi",
        "tipo_pagamento": "Débito",
    },
    {
        "numero_pedido": 2,
        "numero_da_mesa": 5,
        "itens": "Temaki Salmão",
        "quantidade": 3,
        "status": "PREPARANDO",
        "garcom": "Fernanda",
        "observacoes": "Adicionar molho tarê",
        "tipo_pagamento": "Débito",
    },
    {
        "numero_pedido": 3,
        "numero_da_mesa": 8,
        "itens": "Combo Sushi Premium",
        "quantidade": 1,
        "status": "PRONTO",
        "garcom": "Roberto",
        "observacoes": "",
        "tipo_pagamento": "Crédito",
    },
    {
        "numero_pedido": 4,
        "numero_da_mesa": 11,
        "itens": "Hot Roll",
        "quantidade": 12,
        "status": "ENTREGUE",
        "garcom": "Juliana",
        "observacoes": "Cliente pediu guardanapos extras",
        "tipo_pagamento": "PIX",
    },
    {
        "numero_pedido": 5,
        "numero_da_mesa": 14,
        "itens": "Yakisoba de Frango",
        "quantidade": 2,
        "status": "PAGO",
        "garcom": "Marcos",
        "observacoes": "dobro de shoyu",
        "tipo_pagamento": "VR-Refeição",
    }
]


# Funções para testes

def remover_item(pedido):
    print(
        f"\nUm item seria removido do "
        f"pedido nº {pedido['numero_pedido']}."
    )

def adicionar_item_pedido(pedido):
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
# --------------------------------------FIM DO BLOCO DE TESTES --------------------------------------------------


def procurar_pedido(numero_digitado, pedidos):
    '''
    FUNÇÃO AUXILIAR
     Função que procura o pedido dentro da lista de pedido
    (essa lista pode ter sido criada quando a função "criar_pedido()" é executada,
    esta função recebe o nº digitado e a lista criada como parâmetros
    se encontrar a lista vazia, retornará "nada", se não encontrar o valor,
    retornará que o pedido não existe, se encontrar um pedido equivalente ao número registrado,
    retornará o pedido
   '''
    for pedido in pedidos:  # ercorre a lista em busca do pedido numero_pedido é o numero que foi associado lá na criação
        if pedido["numero_pedido"] == numero_digitado:# retorna os dados equivalente a este pedido
            return pedido
    
    return None # aqui caso não encontre ele precisa retornar uma "resposta" negativa (no caso vazia)

def mostrar_pedido(pedido):
    '''
    FUNÇÃO AUXILIAR:
    serve apenas para separar o que vai ser apresentado com a consulta
    tanto para o cliente quanto para o garçom
    '''
    print("\n=============== VISÃO DO CLIENTE ====================")
    print(f"PEDIDO Nº {pedido.get('numero_pedido')}")
    print(f"Garçom: {pedido.get('garcom', 'Não informado')}")
    print(f"Itens: {pedido.get('itens', 'Não informado')} x {pedido.get('quantidade', 'Não informado')}") #inclusão
    print(f"Status: {pedido.get('status', 'Não informado')}")

    '''
    dessa vez optei por uso do .get por uma causa: 
    quando me foi apresentado alguns erros quando quando fiz testes em versões anteriores
    aparecia um erro pois tinha malgumas chaves com erros de digitação, entao uma vez 
    que nao era encontrada a chave me retornava esse erro. o ".get" garante que o programa continue caoe nao ache a chave
    '''

    print("\n=============== VISÃO DO GARÇOM ====================")
    print(f"PEDIDO Nº {pedido.get('numero_pedido')}")
    print(f"Mesa: {pedido.get('numero_da_mesa', 'Não informado')}") 
    print(f"Garçom: {pedido.get('garcom', 'Não informado')}")
    print(f"Itens: {pedido.get('itens', 'Não informado')} x {pedido.get('quantidade', 'Não informado')}") #inclusão
    print(f"Observações: {pedido.get('observacoes', 'Não informado')}") #inclusão
    print(f"Status: {pedido.get('status', 'Não informado')}") #inclusão
    print(f"Pagamento: {pedido.get('tipo_pagamento', 'Não informado')}") #inclusão
    
    valor = pedido.get("valor_total")

    if valor is not None:
        print(f"\nValor total: R$ {valor:.2f}")

    print("====================================")


def consultar_pedido(pedidos):
    '''
    Função principal da consulta.
    executa as duas funções auxiliares:
    Solicita o número, procura o pedido e mostra seus dados.
    Retorna o pedido encontrado ou None.
    '''

    if len(pedidos) == 0:  # verificar se tem algum pedido na lista
        print("\nNão existem pedidos cadastrados.")
        return None

    pedido_encontrado = None # aqui o pedido inicia vazio, só passará a ter valor quando a função for executada no while

    continuar_consulta = "s" # define o valor para o while iniciar o loop
    while continuar_consulta == "s":
        try:
            '''
            ENTENDENDO A LINHA DE BAIXO:
            pega a informação do usuário(input)
            salva em numero_digitado
            em seguida executa a função de consulta baseada no numero digitado
            armazena dentro da variavel pedido_encontrado
            '''
            numero_digitado = int(input("\nDigite o número do pedido que deseja consultar: "))
            pedido_encontrado = procurar_pedido(numero_digitado,pedidos)

            if pedido_encontrado is None:# se não tiver nada na lista ou não encontrar o nº de pedido,ele ainda vai estar como None
                print(
                    f"\nO pedido nº {numero_digitado} não foi encontrado.")
                
            else:#se achar, ele puxa lá da variável que armazenou a execução da função com o numero_digitado
                mostrar_pedido(pedido_encontrado)

            '''
            ENTENDENDO A LINHA ABAIXO:
            essa linha lê a resposta do usuário para continuar
            consultando ou não
            '''
            continuar_consulta = input("\nDeseja realizar outra consulta? (s/n): \n").lower()  # lower para colocar em minusculo

            # valida se foi digitado s ou n:
            while (continuar_consulta != "s" and continuar_consulta != "n"):
                print("\nResposta inválida.")
                continuar_consulta = input("Digite apenas s ou n: ").lower()
        except ValueError:
            print("\nEntrada inválida. Digite somente números.")

    # Verifica se existe um pedido para poder dar opções ao usuário
    if pedido_encontrado != None:
        print("\n=========================================")
        print("Tecle 1 para: Adicionar mais itens")
        print("Tecle 2 para: Remover itens")
        print("Tecle 3 para: Continuar com o pedido atual")
        print("Tecle 4 para: Cancelar o pedido")
        print("Tecle 0 para: Sair")
        print("=========================================")

        opcao = input("\nComo deseja prosseguir? ")  # salva a resposta em opcao

        match opcao: # aqui entra a ligação com as demais funções
            case "1":
                adicionar_item_pedido(pedido_encontrado)
            case "2":
                remover_item(pedido_encontrado)
            case "3":
                print(f"\nO pedido nº {pedido_encontrado['numero_pedido']} continuará sem alterações.")
            case "4":
                cancelar_pedido(pedido_encontrado)
            case "0":
                print("\nSaindo da consulta")
            case _:
                print("\nOpção inválida.")
    else:
        print("\nPedido Inexistente") #se não tem um pedido diferente de None significa que não tem pedidos com essa numeração variável pedido_encontrado ainda possui valor "vazio"
    return pedido_encontrado

'''
Lembrando que cada função vai depender da syntaxe do outro golega de turma
deverá ser ajustado para o nome que ele definir.
'''

# CHAMAR A FUNÇÃO PARA TESTAR:::
consultar_pedido(pedidos)