'''
Código Responsável pelas análises estatísticas e geração de gráficos
será carregado pelo arquivo notebook principal: csv_treatment_1_4.ipynb a partir do bloco N° 14 de códigos

Responsabilidades:
- Conectar o Python ao MySQL usando mysql.connector
- Consultar as tabelas tabela_geral_vendas_2024 e consoles
- Relacionar as tabelas por console_code
- Calcular estatisticas descritivas
- Responder as perguntas do projeto
- Gerar graficos e arquivos CSV com os resultados
'''

# ======= INÍCIO ============

import pandas as pd
import mysql.connector
import matplotlib
matplotlib.use('QtAgg')  # <-- Força o uso da janela do PyQt em vez do Tkinter
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path #biblioteca para transformar objetos em caminhos


# ==========================================================
# 1 - Configurações iniciais
# Definindo variáveis de caminhos 
# ==========================================================

CAMINHO_ARQUIVOS = Path("C:\\Users\dsz_d\\Documents\\Estudos\\SENAC\\BIGDATA\\SenacAnaliseDados2026.2\\UC02\Projeto_final_UC2\\Tratamento_Analise") #caminho em que se encontram os arquivos utilizados
CAMINHO_RESULTADO = Path("C:\\Users\\dsz_d\\Documents\\Estudos\\SENAC\\BIGDATA\\SenacAnaliseDados2026.2\\UC02\\Projeto_final_UC2\\resultado_analises") #caminho onde será salvo os resultados
CAMINHO_GRAFICOS = Path("C:\\Users\\dsz_d\Documents\\Estudos\SENAC\\BIGDATA\\SenacAnaliseDados2026.2\\UC02\\Projeto_final_UC2\\resultado_analises\\graficos") #caminho para salvcar os gráficos


# ==========================================================
# 2. CONEXAO COM O MYSQL
# ==========================================================

# UTILIZANDO O EXEMPLO DA AULA 4 (UC2):
# 1. Conectar ao banco de dados
conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Kitsune#1080",
    database="projeto_games"
)

# 2. Criar um cursor para executar as consultas SQL
cursor = conexao.cursor()


# 3. Definir a consulta SQL
#3.1 = Teste de conexão atnes da conexão real com JOIN:
# query = """
# SELECT *
# FROM tabela_geral_vendas_2024
# LIMIT 10;
# """

#3.2 = Execução da consulta:
query = """
    SELECT
        vendas.id_game,
        vendas.game_name,
        UPPER(TRIM(vendas.console_code))
            AS console_code,
        vendas.genre,
        vendas.publisher,
        vendas.developer,
        vendas.critic_score,
        vendas.total_sales,
        vendas.na_sales,
        vendas.jp_sales,
        vendas.pal_sales,
        vendas.other_sales,
        vendas.game_release_date,
        vendas.last_update_date,
        consoles.id_console,
        consoles.console_name,
        consoles.manufacturer,
        consoles.generation,
        consoles.time_period,
        consoles.console_year,
        consoles.game_media,
        consoles.original_price,
        consoles.total_systems_sold
    FROM tabela_geral_vendas_2024 AS vendas
    LEFT JOIN consoles
        ON UPPER(TRIM(vendas.console_code))
       = UPPER(TRIM(consoles.console_code));
"""

# 4. Executar a consulta
cursor.execute(query)

# 5. Obter todos os resultados
resultados = cursor.fetchall()

# 6. Obter os nomes das colunas retornadas pelo SQL
nomes_colunas = []

for coluna in cursor.description:
    nomes_colunas.append(coluna[0])

# 7. Transformar os resultados em um DataFrame
df_analises = pd.DataFrame(
    resultados,
    columns=nomes_colunas
)

# 8. Exibir uma amostra dos dados
print("\nDADOS CARREGADOS DO MYSQL:")
print(df_analises.head())
print("\nQUANTIDADE DE LINHAS E COLUNAS:")
print(df_analises.shape)
print("\nNOMES DAS COLUNAS:")
print(df_analises.columns.tolist())
print("\nTIPOS DAS COLUNAS:")

df_analises.info()

# 9. Fechar o cursor e a conexão
cursor.close()
conexao.close()

print("\nConexão com o MySQL encerrada.")

#============================================================
# 3. CONVERSÃO DE DADOS PARA EVITAR ERROS:
# ============================================================
'''
cONVERTER COLUNAS PARA DADOS NUMÉRICOS PARA REALIZAR CÁLCULOS
'''
colunas_numericas = [
    "critic_score",
    "total_sales",
    "na_sales",
    "jp_sales",
    "pal_sales",
    "other_sales",
    "original_price",
    "total_systems_sold"
]

for coluna in colunas_numericas:
    df_analises[coluna] = pd.to_numeric(
        df_analises[coluna],
        errors="coerce"
    )

'''
CONVERTER DATAS E CRIAÇÃO DE UMA COLUNA APENAS COM O ANO
PARA FACILITAR A PEQUISA DE HISTÓRICO DE VENDAS 
'''
df_analises["game_release_date"] = pd.to_datetime(
    df_analises["game_release_date"],
    errors="coerce"
)
df_analises["last_update_date"] = pd.to_datetime(
    df_analises["last_update_date"],
    errors="coerce"
)
df_analises["release_year"] = (
    df_analises["game_release_date"].dt.year
)

#============================================================
# 4. CHECAGEM DAS ALTERAÇÕES ANTES DE CONTINUAR
# ============================================================
quantidade_sem_console = (
    df_analises["console_name"].isnull().sum()
)

print("\nQuantidade de registros sem console correspondente:")
print(quantidade_sem_console)

codigos_sem_console = (
    df_analises[
        df_analises["console_name"].isnull()
    ]["console_code"]
    .dropna()
    .drop_duplicates()
    .sort_values()
)

print("\nCodigos sem correspondencia na tabela consoles:")
print(codigos_sem_console.tolist())

print("\nTIPOS DAS COLUNAS APOS AS CONVERSOES:")
df_analises.info() # OBSERVAÇÃO: PRECISA APARECER UMA COLUNA A MAIS (RELEASE_YEAR)

#============================================================
# 5. INÍCIO DOS CÁLCULOS ESTATÍSTICOS
# ============================================================
'''
Define a função que irá fazer as análises de cada indicador
essa função já "prepara" todo os cálculos e cada fez que chamar ela, só preciso passar a séries que eu quero como parâmetro
cada série é uma "coluna" do DATAFRAME
'''
# 5.1 DEFININDO UMA FUNÇÃO PARA ESTATISTICA DESCRITIVA
def calcular_estatisticas(serie):
    """
    Calcula estatisticas descritivas da Serie.
    """

    valores = pd.to_numeric( #transforma os dados em números
        serie,
        errors="coerce" #caso não possa ser convertido, transforma em NaN
    ).dropna() #remove temporariamente os valores vazios

    if valores.empty:
        return pd.Series(dtype="float64") #garante que os cálculos não sejam feitos em uma coluna compeltamente vazia

    q1 = valores.quantile(0.25)
    q2 = valores.quantile(0.50)
    q3 = valores.quantile(0.75)
    iqr = q3 - q1 #intervalo interquartil

    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr

    outliers = valores[ #seleciona os valores qu eestão fora dos limites
        (valores < limite_inferior)
        | (valores > limite_superior)
    ]

    return pd.Series(
        {
            "quantidade": valores.count(),
            "media": valores.mean(),
            "mediana": valores.median(),
            "q1": q1,
            "q2": q2,
            "q3": q3,
            "iqr": iqr,
            "limite_inferior": limite_inferior,
            "limite_superior": limite_superior,
            "quantidade_outliers": outliers.count(),
            "minimo": valores.min(),
            "maximo": valores.max(),
            "amplitude_total": valores.max() - valores.min(),
            "variancia_amostral": valores.var(ddof=1),
            "desvio_padrao_amostral": valores.std(ddof=1),
            "assimetria": valores.skew(),
            "curtose_excesso": valores.kurt()
        }
    )

# 5.2 FUNÇÃO QUE CALCULA A ESTATÍSTICA DAS 5 COLUNAS DE VENDAS DA TABELA
def gerar_estatisticas_vendas(df):
    '''
    Gera estatisticas para vendas globais e regionais.
    Gera uma nova tabela com resultado 
    '''

    colunas = [
        "total_sales", #VENDAS GLOBAIS
        "na_sales", #VENDAS NA AMERICA DO NORTE (EUA)
        "jp_sales", #VENDAS JAPONESAS
        "pal_sales",#VENDAS VENDAS DE REGIÕES DA EUROPA 
        "other_sales" ##OUTRAS VENDAS
    ]

    resultados = {}
    for coluna in colunas:
        print(
            "\nCalculando estatísticas da coluna:",
            coluna
        )
        resultados[coluna] = calcular_estatisticas(
            df[coluna]
        )
    estatisticas = pd.DataFrame(
        resultados
    ).T #".T" é transpor o dataframe (trocar as linhas pelas colunas como se invertesse )

    estatisticas.index.name = (
        "indicador_vendas"
    )
    estatisticas.to_csv(
        CAMINHO_RESULTADO
        / "estatisticas_descritivas_vendas.csv",
        encoding="utf-8",
        index=True
    )
    return estatisticas

#============================================================
# 6. GRÁFICOS
# ===========================================================

def salvar_grafico(nome_arquivo):

    plt.tight_layout()
    plt.savefig(
        CAMINHO_GRAFICOS / nome_arquivo,
        dpi=150,
        bbox_inches="tight"
    )

    plt.show()
    plt.close()


def gerar_histograma_boxplot(df):
    '''
    Gera histograma e boxplot das vendas globais.
    '''

    vendas = df["total_sales"].dropna()

    # Limite visual para evitar que poucos outliers escondam a distribuicao.
    limite_visual = vendas.quantile(0.99)
    vendas_visuais = vendas[vendas <= limite_visual]

    plt.figure(figsize=(10, 6))
    plt.hist(vendas_visuais, bins=30)
    plt.title("Distribuicao das vendas globais ate o percentil 99")
    plt.xlabel("Vendas globais, em milhoes")
    plt.ylabel("Quantidade de jogos")
    salvar_grafico("histograma_vendas_globais.png")

    plt.figure(figsize=(10, 4))
    plt.boxplot(vendas.dropna(), vert=False)
    plt.title("Boxplot das vendas globais")
    plt.xlabel("Vendas globais, em milhoes")
    salvar_grafico("boxplot_vendas_globais.png")


def grafico_barras(
    dados,
    coluna_categoria,
    coluna_valor,
    titulo,
    nome_arquivo,
    top_n=10
):
    '''
    Gera um grafico de barras com os maiores resultados.
    '''

    dados_grafico = (
        dados
        .sort_values(coluna_valor, ascending=False)
        .head(top_n)
        .sort_values(coluna_valor)
    )

    plt.figure(figsize=(11, 6))
    plt.barh(
        dados_grafico[coluna_categoria].astype(str),
        dados_grafico[coluna_valor]
    )
    plt.title(titulo)
    plt.xlabel("Vendas, em milhoes")
    plt.ylabel(coluna_categoria)
    salvar_grafico(nome_arquivo)

#============================================================
# 6.1 TESTANDO ANÁLISES DESCRITIVAS
# ===========================================================

estatisticas_vendas = gerar_estatisticas_vendas(
    df_analises,
)

print("\nESTATÍSTICAS DESCRITIVAS DAS VENDAS:")

print(estatisticas_vendas)

gerar_histograma_boxplot(
    df_analises
)

# ============================================================
# 7. INÍCIO DAS RESPOSTAS PARA CADA PERGUNTA
# ============================================================