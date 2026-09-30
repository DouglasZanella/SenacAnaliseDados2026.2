"""
Arquivo para confirmar os dados das tabelas tratadas (versão 1.0)
importando do arquivo python Table_treatment
"""
from table_treatment_1_2 import (
df_primarysales_2024_tratado,
df_secundarysales_tratado,
df_consoles_tratado
)

print("\nTipos da tabela principal:")
df_primarysales_2024_tratado.info()

print("\nTipos da tabela secundária:")
df_secundarysales_tratado.info()

print("\nTipos da tabela de consoles:")
df_consoles_tratado.info()