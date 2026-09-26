-- CRIANDO MEU BANCO DE DADOS:
CREATE DATABASE meu_ecommerce;

USE meu_ecommerce;

-- CRIANDO A ENTIDADE PRODUTOS:
CREATE TABLE Produtos (
id_produto VARCHAR(10),  
nome VARCHAR(100),
categoria VARCHAR(50),
preco DECIMAL(8,2),
estoque INT
);
-- Remoção de Tabelas/Conteúdo de Tabela:
DROP TABLE Produtos;

SET GLOBAL local_infile = 1; -- marcação de aceite para arquivos locais (passo extra 01 junto ao load data)

-- 'OPT_LOCAL_INFILE=1' -- (passo extra 02 junto ao load data) inserir na sua conexão local (edit da conexão >> Advanced >> Others)

LOAD DATA LOCAL INFILE "C:\\Users\\douglas.portugal\\Documents\\BIGDATA\\CursoBigData2026.2\\UC2\\Aula04\\vendas_clientes.csv" -- Ajuste o caminho no seu banco local
INTO TABLE meu_ecommerce.clientes
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n' -- Aqui: CR LF
IGNORE 1 ROWS -- Pula o cabeçalho 'id_produto,nome...'
(id_cliente, nome, email); -- Mapeia colunas
-- SET preco = REPLACE(@preco_var, '.', '.'); -- Garante que o decimal seja lido corretamente

-- injetando dados na tabela PRODUTO
LOAD DATA LOCAL INFILE "C:\\Users\\douglas.portugal\\Documents\\BIGDATA\\CursoBigData2026.2\\UC2\\Aula04\\vendas_clientes.csv" -- Ajuste o caminho no seu banco local
INTO TABLE meu_ecommerce.produtos
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n' -- Aqui: CR LF
IGNORE 1 ROWS -- Pula o cabeçalho 'id_produto,nome...'
(id_produto, nome, categoria, @preco, estoque); -- Mapeia colunas
SET preco = REPLACE(@preco_var, '.', '.'); -- Garante que o decimal seja lido corretamente

-- CRIANDO A ENTIDADE CLIENTE:
CREATE TABLE Clientes (
id_cliente VARCHAR(10),  
nome VARCHAR(100),
email VARCHAR(30)
);

-- CRIANDO A ENTIDADE PROMOVIDA PEDIDOS:
CREATE TABLE Pedidos (
id_pedido VARCHAR(10),  
id_cliente VARCHAR(10), 
data_pedido DATETIME,
valor_total DECIMAL(10,2),
id_produto VARCHAR(10), 
quantidade SMALLINT
);

-- OPÇÕES DE CONSTRUÇÃO DE CHAVES:
-- 1 - DESDE O CREATE TABLE:
CREATE TABLE pedidos ( 
id_pedido INT auto_increment primary key, 
data_pedido DATE, 
valor_total DECIMAL(10, 2), 
id_cliente INT, 
id_produto INT, 
quantidade INT, 
FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente), 
FOREIGN KEY (id_produto) REFERENCES produtos(id_produto) 
); 

-- 2 - A PARTIR DO ALTER TABLE:
-- 2.1 PK
ALTER TABLE produtos 
ADD CONSTRAINT pk_produtos 
PRIMARY KEY (id_produto);

ALTER TABLE clientes 
ADD CONSTRAINT pk_clientes
PRIMARY KEY (id_cliente);

ALTER TABLE pedidos 
ADD CONSTRAINT pk_pedidos 
PRIMARY KEY (id_pedido);

-- 2.2 FK
ALTER TABLE pedidos 
ADD CONSTRAINT fk_pedidos_clientes 
FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente); 

ALTER TABLE pedidos 
ADD CONSTRAINT fk_pedidos_produtos 
FOREIGN KEY (id_produto) REFERENCES produtos(id_produto);

