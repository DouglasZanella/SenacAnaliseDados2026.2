"""
ARQUIVO PARA TRATAMENTO DOS DADOS CSV
Versão 1.2 = principais melhorias foram: organização da estrutura(facilidade de leitura) , 
renomeação de variáveis e uso de funções para facilitar a leitura
FUÇÕES INCLUÍDAS:
- Uso de lower() para padronizar os cabeçalhos
- Uso de copy() para preservar os DataFrames originais
- uso de shape() para "imprimir" a quantidade de linhas e colunas

Este arquivo realiza a limpeza e a padronização dos arquivos CSV
antes da importação das tabelas para o MySQL.
"""

import pandas as pd


# ============================================================
# 1. TRATAMENTO DO CSV PRINCIPAL DE VENDAS 2024
# ============================================================

df_primarysales_2024_original = pd.read_csv(
    r"C:\Users\dsz_d\Documents\Estudos\SENAC\BIGDATA"
    r"\SenacAnaliseDados2026.2\UC02\Projeto_final_UC2"
    r"\Fonte_Dados_Original\vgchartz-2024.csv"
)
'''
OBSERVAÇÃO:
erros de caminho aconteciam o tempo inteiro, então em algumas pesquisar foi indicado usar:
"r" antes de um caminho para o python ler como RAW STRING (caminho bruto) 
para nao haver erros de interpretação comoo \t ou \n

'''
# Cria uma cópia para preservar o DataFrame original
df_primarysales_2024_tratado = (
    df_primarysales_2024_original.copy()
)

# Remove a coluna de imagens
df_primarysales_2024_tratado = (
    df_primarysales_2024_tratado.drop(
        columns=["img"]
    )
)

# Renomeia as colunas
df_primarysales_2024_tratado = (
    df_primarysales_2024_tratado.rename(
        columns={
            "title": "game_name",
            "console": "console_code",
            "release_date": "game_release_date",
            "last_update": "last_update_date"
        }
    )
)

print("\nCSV PRINCIPAL DE VENDAS 2024:")
print(df_primarysales_2024_tratado.head())

print("\nQuantidade de linhas e colunas:")
print(df_primarysales_2024_tratado.shape)

print("\n", "=" * 80)


# ============================================================
# 2. TRATAMENTO DO CSV SECUNDÁRIO DE VENDAS
# ============================================================

df_secundarysales_original = pd.read_csv(
    r"C:\Users\dsz_d\Documents\Estudos\SENAC\BIGDATA"
    r"\SenacAnaliseDados2026.2\UC02\Projeto_final_UC2"
    r"\Fonte_Dados_Original\video_games_sales.csv"
)

# Cria uma cópia para preservar o DataFrame original
df_secundarysales_tratado = (
    df_secundarysales_original.copy()
)

# Tratamento maiusculo -> minusculo 
df_secundarysales_tratado.columns = (
    df_secundarysales_tratado.columns.str.lower()
)

# Renomeia colunas para padronizar com o projeto
df_secundarysales_tratado = (
    df_secundarysales_tratado.rename(
        columns={
            "rank": "game_rank",
            "name": "game_name",
            "platform": "console_code",
            "year": "game_year",
            "global_sales": "total_sales"
        }
    )
)

print("\nCSV SECUNDÁRIO DE VENDAS:")
print(df_secundarysales_tratado.head())

print("\nQuantidade de linhas e colunas:")
print(df_secundarysales_tratado.shape)

print("\n", "=" * 80)


# ============================================================
# 3. TRATAMENTO DO CSV DE CONSOLES
# ============================================================

df_consoles_original = pd.read_csv(
    r"C:\Users\dsz_d\Documents\Estudos\SENAC\BIGDATA"
    r"\SenacAnaliseDados2026.2\UC02\Projeto_final_UC2"
    r"\Fonte_Dados_Original\videogameconsoles.csv"
)

# Copia o original
df_consoles_tratado = df_consoles_original.copy()

#  Tratamento maiusculo -> minusculo 
df_consoles_tratado.columns = (
    df_consoles_tratado.columns.str.lower()
)

# Padroniza os nomes das colunas
df_consoles_tratado = df_consoles_tratado.rename(
    columns={
        "id": "id_console",
        "consolename": "console_name",
        "year": "console_year"
    }
)

print("\nCSV DE CONSOLES:")
print(df_consoles_tratado.head())

print("\nQuantidade de linhas e colunas:")
print(df_consoles_tratado.shape)

print("\n", "=" * 80)


# ============================================================
# 4. SALVAMENTO DOS ARQUIVOS TRATADOS
# ============================================================
# - RETIRE OS COMENTÁRIOS NO 1º USO, DEPOIS PODE COMENTAR PARA NÃO FICAR USANDO 
# ============================================================

# df_primarysales_2024_tratado.to_csv(
#     r"C:\Users\dsz_d\Documents\Estudos\SENAC\BIGDATA"
#     r"\SenacAnaliseDados2026.2\UC02\Projeto_final_UC2"
#     r"\Fonte_Dados_tratados\video_games_sales_2024_tratado.csv",
#     index=False,
#     sep=",",
#     encoding="utf-8"
# )

# df_secundarysales_tratado.to_csv(
#     r"C:\Users\dsz_d\Documents\Estudos\SENAC\BIGDATA"
#     r"\SenacAnaliseDados2026.2\UC02\Projeto_final_UC2"
#     r"\Fonte_Dados_tratados\video_games_sales_secundaria_tratado.csv",
#     index=False,
#     sep=",",
#     encoding="utf-8"
# )

# df_consoles_tratado.to_csv(
#     r"C:\Users\dsz_d\Documents\Estudos\SENAC\BIGDATA"
#     r"\SenacAnaliseDados2026.2\UC02\Projeto_final_UC2"
#     r"\Fonte_Dados_tratados\consoles_tratado.csv",
#     index=False,
#     sep=",",
#     encoding="utf-8"
# )

print("\nSalvamento dos arquivos CSV concluído com sucesso!")