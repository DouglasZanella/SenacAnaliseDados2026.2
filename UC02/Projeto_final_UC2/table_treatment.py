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
df_secundaryvgsales_renametitle = df_secundary_vgsales.rename(columns={'Platform':'console'}) #renomeia a coluna de plataforma para console

print(df_secundaryvgsales_renametitle)
print("\n", "="*80)

# 3- CSV CONSOLES: 
df_consoles = pd.read_csv('Fonte_Dados_Original/videogameconsoles.csv')
df_consoles_renamecolumn = df_consoles.rename(columns={df_consoles.columns[0]: "id_console", df_consoles.columns[1]: "console", df_consoles.columns[3]: "console_year"  })
print(df_consoles_renamecolumn)
print("\n", "="*80)

# ARMAZENANDO EM UMA VARIÁVEL FORMATADA PARA MELHOR ENTENDIMENTO: 

df_vgsales2024_tratado = df_vgasales2024_renametitle
df_secundary_vgsales_tratado = df_vgasales2024_renametitle
df_console_tratado = df_consoles_renamecolumn

# SALVA OS ARQUIVOS CSV TRATADOS NA PSTA DE FONTE_DADOS_TRATADOS::
# df_vgsales2024_tratado.to_csv('C:\\Users\\douglas.zanella\\Documents\\BIGDATA\\SenacAnaliseDados2026.2\\UC02\\Projeto_final_UC2\\Fonte_Dados_tratados\\df_vgsales2024_tratado.csv', index=False, sep=',', encoding='utf-8')
# df_secundary_vgsales_tratado.to_csv('C:\\Users\\douglas.zanella\\Documents\\BIGDATA\\SenacAnaliseDados2026.2\\UC02\\Projeto_final_UC2\\Fonte_Dados_tratados\\df_secundary_vgsales_tratado.csv', index=False, sep=',', encoding='utf-8')
df_console_tratado.to_csv('C:\\Users\\douglas.zanella\\Documents\\BIGDATA\\SenacAnaliseDados2026.2\\UC02\\Projeto_final_UC2\\Fonte_Dados_tratados\\df_console_tratado.csv', index=False, sep=',', encoding='utf-8')