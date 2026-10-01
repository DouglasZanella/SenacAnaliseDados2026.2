-- TABELAS DE CONSULTA PROJETO_FINAL

-- criando o banco de dados dos jogos
CREATE DATABASE projeto_games;

-- "Ativando o Bando de dados criado" 
USE projeto_games;

-- CRIANDO A TABELA PARA INJETAR OS DADOS:
CREATE TABLE video_games_sales_2024(
	game_name VARCHAR(100),
    console_code VARCHAR(100),
    genre VARCHAR(50),
    publisher VARCHAR(100),
    developer VARCHAR(100),
    critic_score DECIMAL(10,2),
    total_sales DECIMAL(10,2),
    na_sales DECIMAL(10,2),
    jp_sales DECIMAL(10,2),
	pal_sales DECIMAL(10,2),
    other_sales DECIMAL(10, 2),
    release_date DATETIME,
    last_update DATETIME
);

CREATE TABLE secundary_vgsales_2024(
	game_rank TINYINT,
    game_name VARCHAR(100),
    console_code VARCHAR (100),
    game_year INT,
    genre VARCHAR (100),
    publisher VARCHAR (100),
    na_sales DECIMAL (10,2),
    eu_sales DECIMAL (10,2),
	jp_sales DECIMAL (10,2),
    other_sales DECIMAL (10,2),
    global_sales DECIMAL(10, 2)
);
    
CREATE TABLE consoles(
	id_consoles INT,
    console_name VARCHAR(100),
    manufacturer VARCHAR(100),
    console_year VARCHAR(10),
    generation VARCHAR(10)
);

SET GLOBAL local_infile = 1; -- marcação de aceite para arquivos locais (passo extra 01 junto ao load data)

-- 'OPT_LOCAL_INFILE=1' -- (passo extra 02 junto ao load data) inserir na sua conexão local (edit da conexão >> Advanced >> Others)

-- INJETANDO OS DADOS EM CADA TABELA - BASE DE VENDAS DOS JOGOS:
LOAD DATA LOCAL INFILE 'C:\\Users\\douglas.zanella\\Documents\\BIGDATA2026\\SenacAnaliseDados2026.2\\UC02\\Projeto_final_UC2\\Fonte_Dados_tratados\\video_games_sales_2024_tratado.csv' -- Ajuste o caminho no seu banco local
INTO TABLE video_games_sales_2024
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n' -- Aqui: CR LF
IGNORE 1 ROWS -- Pula o cabeçalho 'id_produto,nome...'
(game_name, console_code, genre, publisher, developer, critic_score, total_sales, na_sales, jp_sales, pal_sales, other_sales, release_date, last_update); -- Mapeia colunas
-- (game_name, console, genre, publisher, developer, @critic_score, @total_sales, @na_sales, @jp_sales, @pal_sales, @other_sales, release_date, last_update) -- Mapeia colunas
-- SET critic_score = REPLACE(@critic_score, '.', '.'); -- Garante que o decimal seja lido corretamente 
-- SET total_sales = REPLACE(@total_sales, '.', '.'); -- Garante que o decimal seja lido corretamente 
-- SET na_sales = REPLACE(@na_sales, '.', '.'); -- Garante que o decimal seja lido corretamente 
-- SET jp_sales = REPLACE(@jp_sales, '.', '.'); -- Garante que o decimal seja lido corretamente 
-- SET pal_sales = REPLACE(@pal_sales, '.', '.'); -- Garante que o decimal seja lido corretamente 
-- SET other_sales = REPLACE(@other_sales, '.', '.'); -- Garante que o decimal seja lido corretamente 
-- ---------------------------------------------------------------------------------------------------------------------------
-- INJETANDO OS DADOS EM CADA TABELA - BASE SECUNDÁRIA DE VENDAS DOS JOGOS:
LOAD DATA LOCAL INFILE 'C:\\Users\\douglas.zanella\\Documents\\BIGDATA2026\\SenacAnaliseDados2026.2\\UC02\\Projeto_final_UC2\\Fonte_Dados_tratados\\video_games_sales_secundaria_tratado.csv' -- Ajuste o caminho no seu banco local
INTO TABLE secundary_vgsales_2024
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n' -- Aqui: CR LF
IGNORE 1 ROWS -- Pula o cabeçalho 'id_produto,nome...'
(game_rank, game_name, console_code, game_year, genre, publisher, na_sales, eu_sales, jp_sales, other_sales, global_sales); -- Mapeia colunas; -- Mapeia colunas

-- ---------------------------------------------------------------------------------------------------------------------------

-- INJETANDO OS DADOS EM CADA TABELA - CONSOLE
LOAD DATA LOCAL INFILE 'C:\\Users\\douglas.zanella\\Documents\\BIGDATA2026\\SenacAnaliseDados2026.2\\UC02\\Projeto_final_UC2\\Fonte_Dados_tratados\\consoles_tratado.csv' -- Ajuste o caminho no seu banco local
INTO TABLE consoles
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n' -- Aqui: CR LF
IGNORE 1 ROWS -- Pula o cabeçalho 'id_produto,nome...'
(id_consoles,console_name, manufacturer, console_year, generation);

ALTER TABLE video_games_sales_2024 
DROP COLUMN pk_id_game;

-- ALTER TABLE PARA INCLUIR COLUNAS NECESSÁRIAS
ALTER TABLE video_games_sales_2024 
ADD COLUMN pk_id_game INT NOT NULL AUTO_INCREMENT; 


-- ALTER TABLE PARA INCLUIR CHAVES
ALTER TABLE video_games_sales_2024 	
ADD CONSTRAINT PK_video_games_sales_2024
PRIMARY KEY (id_games); 

ALTER TABLE video_games_sales_2024 
ADD CONSTRAINT fk_video_games_sales_2024_consoles 
FOREIGN KEY (id_consoles) REFERENCES consoles(cid_consoles); 

ALTER TABLE secundary_vgsales_2024 
ADD CONSTRAINT pk_secundary_vgsales_2024 
PRIMARY KEY (id_games);

ALTER TABLE consoles 
ADD CONSTRAINT pk_consoles 
PRIMARY KEY (id_consoles);

-- =========================================================
-- EXCLUIR AS TABELAS:::
DROP TABLE video_games_sales_2024;
DROP TABLE secundary_vgsales_2024;
DROP TABLE consoles;
