-- Criando Banco de Dados
-- iniciada na aula 05

CREATE DATABASE meu_ecommerce;

USE meu_ecommerce;

-- CRIANDO A ENTIDADE PRODUTOS
CREATE TABLE produtos (
id_produto VARCHAR(10),
nome VARCHAR(100),
categoria VARCHAR(50),
preco DECIMAL(8,2),
estoque INT
);

-- Remoção de tabelas/ conteúdo de Tabela:
DROP TABLE produtos;

SET GLOBAL local_infile = 1; -- marcação de aceite para arquivos locais (passo extra 01 junto ao load data)

-- 'OPT_LOCAL_INFILE=1' -- (passo extra 02 junto ao load data) inserir na sua conexão local (edit da conexão >> Advanced >> Others)

LOAD DATA LOCAL INFILE 'C:\\Users\\douglas.zanella\\Documents\\BIGDATA\\SenacAnaliseDados2026.2\\UC02\\Aula05\\vendas_produtos.csv' -- Ajuste o caminho no seu banco local
INTO TABLE meu_ecommerce.produtos
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n' -- Aqui: CR LF
IGNORE 1 ROWS -- Pula o cabeçalho 'id_produto,nome...'
(id_produto, nome, categoria, @preco_var, estoque) -- Mapeia colunas
SET preco = REPLACE(@preco_var, '.', '.'); -- Garante que o decimal seja lido corretamente

-- CRIANDO A ENTIDADE CLIENTE
CREATE TABLE clientes (
id_cliente VARCHAR(10),
nome VARCHAR(100),
email VARCHAR(30)
);

SET GLOBAL local_infile = 1; -- marcação de aceite para arquivos locais (passo extra 01 junto ao load data)

-- 'OPT_LOCAL_INFILE=1' -- (passo extra 02 junto ao load data) inserir na sua conexão local (edit da conexão >> Advanced >> Others)

LOAD DATA LOCAL INFILE 'C:\\Users\\douglas.zanella\\Documents\\BIGDATA\\SenacAnaliseDados2026.2\\UC02\\Aula05\\vendas_clientes.csv' -- Ajuste o caminho no seu banco local
INTO TABLE meu_ecommerce.clientes
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n' -- Aqui: CR LF
IGNORE 1 ROWS -- Pula o cabeçalho 'id_cliente,nome,email'
(id_cliente,nome,email); -- Mapeia colunas

-- CRIANDO A ENTIDADE PEDIDOS
CREATE TABLE pedidos (
id_pedido VARCHAR(10),
id_cliente VARCHAR(10),
data_pedido DATETIME,
valor_total DECIMAL(10,2),
id_produto VARCHAR(10),
quantidade SMALLINT
);

LOAD DATA LOCAL INFILE 'C:\\Users\\douglas.zanella\\Documents\\BIGDATA\\SenacAnaliseDados2026.2\\UC02\\Aula05\\vendas_pedidos.csv' -- Ajuste o caminho no seu banco local
INTO TABLE meu_ecommerce.pedidos
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n' -- Aqui: CR LF
IGNORE 1 ROWS -- Pula o cabeçalho
(id_pedido, id_cliente, data_pedido, valor_total, id_produto, quantidade); -- Mapeia colunas

-- OPÇÕES DE CONSTRUÇÃO DE CHAVES
-- 1 - DESDE O CREATE TABLET
CREATE TABLE pedidos (
id_pedido INT AUTO_INCREMENT PRIMARY KEY,
id_cliente VARCHAR(10),
data_pedido DATETIME,
valor_total DECIMAL(10,2),
id_produto VARCHAR(10),
quantidade SMALLINT,
FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente), -- precisa ter uma linha de chave estrangeira para cada chave estangeira
FOREIGN KEY (id_produto) REFERENCES Produtos(id_produto)
);
-- 2 - A PARTIR DO ALTER TABLE
ALTER TABLE pedidos
ADD CONSTRAINT fk_pedidos_clientes
FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente);

ALTER TABLE pedidos
ADD CONSTRAINT fk_pedidos_produtos
FOREIGN KEY (id_produto) REFERENCES produtos(id_produto);

ALTER TABLE produtos
ADD CONSTRAINT pk_produtos
PRIMARY KEY (id_produto);

ALTER TABLE clientes
ADD CONSTRAINT pk_clientes
PRIMARY KEY (id_cliente);

ALTER TABLE pedidos
ADD CONSTRAINT pk_pedidos
PRIMARY KEY (id_pedido);