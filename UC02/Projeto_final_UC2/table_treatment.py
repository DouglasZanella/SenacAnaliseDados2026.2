#ARQUIVO PARA TRATAMENTO DOS DADOS CSV
'''
ARQUIVO QUE REALIZARÁ AS LIMPEZAS DOS ARQUIVOS CSV ANTES DE INJETAR NAS TABELAS DO SQL
'''
import pandas as pd
import numpy as np

# 1 -CSV PRINCIPAL :
df_vgsales2024 = pd.read_csv('Fonte_Dados_Original/vgchartz-2024.csv')
df_vgsales2024_remove_imgcolumns = df_vgsales2024.drop(df_vgsales2024.columns[0], axis=1) #Remove a primeira coluna do CSV referente as imagens
df_vgasales2024_renametitle = df_vgsales2024_remove_imgcolumns.rename(columns={'title':'game_name'}) #renomeia a coluna de titulo para nome

print(df_vgasales2024_renametitle)
print("\n", "="*80)

# 2 -CSV SECUNDÁRIO :

df_secundary_vgsales = pd.read_csv('Fonte_Dados_Original/video_games_sales.csv')
df_secundary_vgsales_renamecolumn = df_secundary_vgsales.rename(columns={df_secundary_vgsales.columns[0]: "id_game"}) #renomeia o título da coluna 1 de "Rank" para "Id_Game"

print(df_secundary_vgsales_renamecolumn)
print("\n", "="*80)

# 3- CSV CONSOLES: 
df_consoles = pd.read_csv('Fonte_Dados_Original/videogameconsoles.csv')
df_consoles_renamecolumn = df_consoles.rename(columns={df_consoles.columns[0]: "id_console", df_consoles.columns[3]: "console_year" }) #renomeia o título da coluna 1 de "ID" para "id_console"

print(df_consoles_renamecolumn)
print("\n", "="*80)