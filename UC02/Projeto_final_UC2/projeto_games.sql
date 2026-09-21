-- TABELAS DE CONSULTA PROJETO_FINAL

-- criando o banco de dados dos jogos
CREATE DATABASE projeto_games;

-- "Ativando o Bando de dados criado" 
USE projeto_games;

-- CRIANDO A TABELA PARA INJETAR OS DADOS:
CREATE TABLE video_games_sales_2024(
	img 
    title VARCHAR(100),
    console VARCHAR(100),
    genre VARCHAR (50),
    publisher VARCHAR (100),
    developer VARCHAR (100),
    critic_score DECIMAL (10,2),
    total_sales DECIMAL (10,2),
    na_sales DECIMAL (10,2),
    jp_sales DECIMAL (10,2),
	pal_sales DECIMAL (10,2),
    other_sales(10, 2),
    release_date DATETIME,
    last_update (DATETIME);
)
