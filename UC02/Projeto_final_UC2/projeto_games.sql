-- TABELAS DE CONSULTA PROJETO_FINAL

-- criando o banco de dados dos jogos
CREATE DATABASE projeto_games;

-- "Ativando o Bando de dados criado" 
USE projeto_games;

-- -------------------------------------------- / CRIA A TABELA VENDAS CONSOLE / ----------------------------------------------
CREATE TABLE consoles (
    id_console INT NOT NULL,
    console_code VARCHAR(20) NOT NULL,
    console_name VARCHAR(150) NOT NULL,
    manufacturer VARCHAR(100),
    generation VARCHAR(30),
    time_period VARCHAR(30),
    console_year INT,
    game_media VARCHAR(255),
    original_price DECIMAL(10, 2),
    total_systems_sold BIGINT,
    CONSTRAINT pk_consoles
        PRIMARY KEY (id_console),
    CONSTRAINT uq_consoles_console_code
        UNIQUE (console_code)
);

-- -------------------------------------------- /CRIA A TABELA VENDAS GERAIS / ----------------------------------------------

CREATE TABLE tabela_geral_vendas_2024 (
    id_game INT NOT NULL,
    game_name VARCHAR(255) NOT NULL,
    console_code VARCHAR(20),
    genre VARCHAR(100),
    publisher VARCHAR(255),
    developer VARCHAR(255),
    critic_score DECIMAL(4,2),
    total_sales DECIMAL(12,4),
    na_sales DECIMAL(12,4),
    jp_sales DECIMAL(12,4),
    pal_sales DECIMAL(12,4),
    other_sales DECIMAL(12,4),
    game_release_date DATE,
    last_update_date DATE,

    CONSTRAINT pk_tabela_geral_vendas
        PRIMARY KEY (id_game)
);

-- -------------------------------------------- / / -------------------------------------------------------------------------------

SET GLOBAL local_infile = 1; -- marcação de aceite para arquivos locais (passo extra 01 junto ao load data)
-- 'OPT_LOCAL_INFILE=1' -- (passo extra 02 junto ao load data) inserir na sua conexão local (edit da conexão >> Advanced >> Others)

-- -------------------------------------------- / INJETA DADOS NA TABELA VENDAS GERAIS / ----------------------------------------------

-- Versão CURSO:'C:\\Users\\douglas.zanella\\Documents\\BIGDATA2026\\SenacAnaliseDados2026.2\\UC02\\Projeto_final_UC2\\Fonte_Dados_tratados\\video_games_sales_2024_tratado.csv'
-- VERSÃO CASA: "C:\\Users\\dsz_d\\Documents\\Estudos\\SENAC\\BIGDATA\\SenacAnaliseDados2026.2\\UC02\\Projeto_final_UC2\\Fonte_Dados_tratados\\tabela_geral_vendas_2024.csv"
LOAD DATA LOCAL INFILE "C:\\Users\\dsz_d\\Documents\\Estudos\\SENAC\\BIGDATA\\SenacAnaliseDados2026.2\\UC02\\Projeto_final_UC2\\Fonte_Dados_tratados\\tabela_geral_vendas_2024.csv"
INTO TABLE tabela_geral_vendas_2024
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n' -- Aqui: CR LF
IGNORE 1 ROWS -- Pula o cabeçalho 'id_produto,nome...'
(id_game, game_name, console_code, genre, publisher, developer, @critic_score, @total_sales, @na_sales, @jp_sales, @pal_sales, @other_sales, @game_release_date, @last_update_date)
SET
    critic_score = NULLIF(@critic_score, ''),
    total_sales = NULLIF(@total_sales, ''),
    na_sales = NULLIF(@na_sales, ''),
    jp_sales = NULLIF(@jp_sales, ''),
    pal_sales = NULLIF(@pal_sales, ''),
    other_sales = NULLIF(@other_sales, ''),
    game_release_date = NULLIF(
        LEFT(@game_release_date, 10),
        ''
    ),
    last_update_date = NULLIF(
        LEFT(@last_update_date, 10),
        ''
    );
    
-- -------------------------------------------- / INJETA DADOS NA TABELA CONSOLE / ----------------------------------------------

LOAD DATA LOCAL INFILE "C:/Users/dsz_d/Documents/Estudos/SENAC/BIGDATA/SenacAnaliseDados2026.2/UC02/Projeto_final_UC2/Fonte_Dados_tratados/videogameconsoles.csv"
INTO TABLE consoles
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id_console, console_code, console_name, manufacturer, generation, time_period, @console_year, game_media, @original_price, @total_systems_sold )
SET
    console_year = NULLIF(
            TRIM(@console_year),
            ''
),
    original_price = NULLIF(
            TRIM(@original_price),
            '' 
),
    total_systems_sold = NULLIF(
            TRIM( REPLACE( @total_systems_sold, '\r', '') 
            ),
		''
);
-- -------------------------------------------- / VERIFICAR QUANTIDADES / ---------------------------------------------------------

-- ================= QUANTIDADE CONSOLES
SELECT
    COUNT(*) AS quantidade_consoles
FROM consoles;

-- ================= QUANTIDADE JOGOS
SELECT
    COUNT(*) AS quantidade_jogos
FROM tabela_geral_vendas_2024;

-- -------------------------------------------- / VISUALIZAÇÕES / ---------------------------------------------------------
SELECT *
FROM consoles
LIMIT 10;

SELECT *
FROM tabela_geral_vendas_2024
LIMIT 10;

-- -------------------------------------------- / CONFERÊNCIA DE DUPLICATAS / ---------------------------------------------------------
SELECT
    console_code,
    COUNT(*) AS quantidade

FROM consoles

GROUP BY console_code

HAVING COUNT(*) > 1;

-- -------------------------------------------- / TESTE DE RELACIONAMENTO / ---------------------------------------------------------
SELECT
    vendas.id_game,
    vendas.game_name,
    vendas.console_code,
    vendas.genre,
    vendas.total_sales,

    consoles.console_name,
    consoles.manufacturer,
    consoles.generation

FROM tabela_geral_vendas_2024 AS vendas

LEFT JOIN consoles
    ON vendas.console_code = consoles.console_code

LIMIT 100;

-- CONSULTA DE DE DADOS INEXISTENTES ENTRE AS TABELAS

SELECT DISTINCT
    vendas.console_code

FROM tabela_geral_vendas_2024 AS vendas

LEFT JOIN consoles
    ON vendas.console_code = consoles.console_code

WHERE consoles.console_code IS NULL

ORDER BY vendas.console_code;

-- -------------------------------------------- / / -------------------------------------------------------------------------------


-- EXCLUIR AS TABELAS 
DROP TABLE tabela_geral_vendas_2024;
DROP TABLE consoles;

-- VERIFICA CONEXÃO 
SHOW GLOBAL VARIABLES LIKE 'local_infile';