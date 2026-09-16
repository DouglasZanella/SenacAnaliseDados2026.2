#Código das atividades do PDF 01
#LeiturasExcel_Python_Ver1.0

import pandas as pd


df_transacao = pd.read_excel("base_invest.xlsx", sheet_name="Transacoes")#lê a planilha e pega apenas as transações
print(df_transacao)

'''
Pergunta 1:
●  Quais são as máximas e mínimas de operação de compra e venda das transações? 
'''

df_compras = df_transacao.query("operacao == 'compra'")#separa as ações de compra
df_vendas = df_transacao.query("operacao == 'venda'")#separa as ações de venda

maior_compra = df_compras['preco'].max()#retorna o maior valor de compra
menor_compra = df_compras['preco'].min()#retorna o menor valor de compra

maior_vendas = df_vendas['preco'].max()#retorna o maior valor de Venda
menor_vendas = df_vendas['preco'].min()#retorna o menor valor de Venda


print("=" * 20, "COMPRAS", "="*20)
print(f"\n o Maior valor de compra foi de:\n {maior_compra:.2f}")
print(f"\n o Menor valor de compra foi de:\n {menor_compra:.2f}")

print("=" * 20, "VENDAS", "="*20)
print(f"\n o Maior valor de Vendas foi de:\n {maior_vendas:.2f}")
print(f"\n o Menor valor de Vendas foi de:\n {menor_vendas:.2f}")

'''
Pergunta 2: 
●  Qual CNPJ tem o ativo de maior valor? 
'''
#Leio a aba de ativos
df_ativo = pd.read_excel("base_invest.xlsx", sheet_name="Ativo")

#para saber qual o maior ativo, preciso calcular a quantidade do ativo*o valor deles para achar o maior preço 
df_transacao['valor_total'] = (df_transacao['quantidade'] * df_transacao['preco']) #cria a coluna com o total de cada transação
print("=" * 20, "TOTAL POR TRANSAÇÃO", "="*20)
print(df_transacao['valor_total'])

#separo os valores por cada um dos Ativos
valor_por_ativo = df_transacao.groupby("id_ativo")['valor_total'].sum() #soma o total de transações por cada ID do Ativo (coluna Id_Ativo)
print("=" * 20, "TOTAL DE CADA ATIVO", "="*20)
print(valor_por_ativo)

#Verifico qual dos ativos tem maior valor e salvo o ID 
'''
originalmente eu escrevi:
indice_maior_preco = df_transacao['preco'].idxmax()
e aqui ele ta verificando o dado errado.
'''
indice_maior_preco = df_transacao['valor_total'].idxmax()#PROCURAR PELO INDICE DO VALOR TOTAL 
#com esse dado eu procuro a linha que tem o maior preco
linha_maior_preco = df_transacao.loc[indice_maior_preco]
#com esse dado verifico o id do ativo que está na linha com maior aitvo:
id_ativo_maior_valor = linha_maior_preco['id_ativo']
#com tudo isso agora eu consigo chegar no ID do maior ativo e comparar na aba de ativo qual o CNPJ que está relacionado com essa linha: 
linha_maior_ativo = df_ativo[df_ativo['id_ativo'] == id_ativo_maior_valor]
cnpj_id_ativo_maior_valor = linha_maior_ativo.iloc[0]['cnpj']

print("=" * 20, "ATIVO DE MAIOR VALOR", "="*20)
print(f"ID do ativo: {id_ativo_maior_valor}")
print(f"CNPJ: {cnpj_id_ativo_maior_valor}")


'''
Pergunta 3:
●  Qual valor total em transações de cada participante?
'''
valor_por_participante = df_transacao.groupby('id_participante')["valor_total"].sum() #Soma o total de transações por cada participante
print("=" * 20, "TOTAL POR PARTICPANTE", "="*20)
print(valor_por_participante)