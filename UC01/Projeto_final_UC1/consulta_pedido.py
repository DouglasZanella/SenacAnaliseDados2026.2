#função consultar_pedido() do projeto final

#criação de uma lista "falsa" para testes:::::
lista_pedidos = [
    {
        "numero_pedido": 20, 
        "mesa": 4, 
        "status": "PREPARANDO", 
        "pagamento": "PENDENTE", 
        "garcom":"José",
        "valor_total":105.98
    },
    { 
        "numero_pedido": 21, 
        "mesa": 7, 
        "status": "PRONTO", 
        "pagamento": "PENDENTE", 
        "garcom":"Cleiton",
        "valor_total":75.90
    } 
]
#--------------------------------------------

#FUNÇÕES AUXILIARES PARA TESTAR::::
def remover_pedido():
    execucao = "item removido"
    return execucao

def adicionar_pedido():
    execucao = "item adicionado"
    return execucao

def cancelar_pedido():
    execucao = "Pedido Cancelado"
    return execucao
#___________________________________________________________

# def mostra_tela(pedido):
#     apresentacao = print(
#         "\n==============================================="
#         f"\n| SEUS PEDIDOS |"
#         "\n==============================================="
#     )
#     pedido = consultar_pedidos()
#     if pedido is None: 
#         print("\nPedido não encontrado ou número inválido.") 
#     else: 
#         print("\n========== DADOS DO PEDIDO ==========") 
#         print(f"Número: {pedido['numero_pedido']}") 
#         print(f"Mesa: {pedido['mesa']}") 
#         print(f"Garçom: {pedido['garcom']}") 
#         print(f"Status: {pedido['status']}") 
#         print(f"Pagamento: {pedido['pagamento']}") 
#         print(f"Total: R$ {pedido['valor_total']:.2f}")    
#         return pedido

def consultar_pedidos():  
    '''
    Função que procura o pedido dentro da lista de pedido,
    informada pelo sistema (essa lista pode ter sido criada 
    quando a função "criar_pedido()" é executada, 
    portanto o Nº fiará registrado e poderei acessar com a Consulta, 
    se encontrar a lsita vazia, retornará "nada", se não encontrar o valor,
    retornará que o pedido não existe, se encontrar um pedido equivalente ao número registrado,
    retornará o pedido(com os valores do diciário criado para cada item da lista 
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
            return None
        consulta = input("Desejo continuar a consulta? (s/n)\n")
    except ValueError:
        print("Entrada inválida. Digite somente números.") 
        return None
    
        
    


# TESTE PARA VER SE A FUNÇÃO ESTÁ RETORTANDO CORRETAMENTE:::::: 
while True : 
    pedido = consultar_pedidos()
    if pedido != None: 
        print("\n========== DADOS DO PEDIDO ==========") 
        print(f"Número: {pedido['numero_pedido']}") 
        print(f"Mesa: {pedido['mesa']}") 
        print(f"Garçom: {pedido['garcom']}") 
        print(f"Status: {pedido['status']}") 
        print(f"Pagamento: {pedido['pagamento']}") 
        print(f"Total: R$ {pedido['valor_total']:.2f}")
        
print("\n=========================================") 
print("\nTecle 1 para: Adicionar mais itens"
"\nTecle 2 para: Remover Itens"
"\nTecle 3 para: Continuar com o Pedido atual"
"\nTecle 4 para: Cancelar o Pedido"
)  

print("\n=========================================\n")
resp = input("Com odeseja prosseguir? -> TECLE 1 | 2 | 3 | 4")
try:
    match resp:
        case 1:
            adicionar_pedido(resp)
        case 2:
            remover_pedido(resp)
        case 3:
            cancelar_pedido(resp)
        case _:
            print("Entrada inválida")
except ValueError:
    print("Entada inválida, digite novamente")

