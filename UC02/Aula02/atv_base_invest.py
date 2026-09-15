#Código das atividades do PDF 01
#LeiturasExcel_Python_Ver1.0

import pandas as pd


transacao_invest = pd.read_excel("base_invest.xlsx", sheet_name="Transacoes")#lê a planilha e pega apenas as transações
ativo_invest = pd.read_excel("base_invest.xlsx", sheet_name="Ativo")

print(transacao_invest)
compras_invest = transacao_invest.query("operacao == 'compra'")
vendas_invest = transacao_invest.query("operacao == 'venda'")
transacao_invest['qtd_invest'] = transacao_invest['quantidade'] * transacao_invest['preco']
print(qtd_invest)

valor_por_ativo = transacao_invest.groupby("id_ativo")['valor_total'].sum()

print(qtd_invest)

max_compra_invest = compras_invest['preco'].max()
min_compra_invest = compras_invest['preco'].min()

max_venda_invest = vendas_invest['preco'].max()
min_venda_invest = vendas_invest['preco'].min()


print("=" * 20, "COMPRAS", "="*20)
print(compras_invest)

print("=" * 20, "VENDAS", "="*20)
print(vendas_invest)

print("=" * 20, "VALOR MÁXIMO DE COMPRA", "="*20)
print(f"\n o Maior valor de compra foi de:\n {max_compra_invest:.2f}")

print("=" * 20, "VALOR MÍNIMO DE COMPRA", "="*20)
print(f"\n o Menor valor de compra foi de:\n {min_compra_invest:.2f}")

print("=" * 20, "VALOR MÁXIMO DE VENDA", "="*20)
print(f"\n o Maior valor de compra foi de:\n {max_venda_invest:.2f}")

print("=" * 20, "VALOR MÍNIMO DE VENDA", "="*20)
print(f"\n o Menor valor de compra foi de:\n {min_venda_invest:.2f}")
