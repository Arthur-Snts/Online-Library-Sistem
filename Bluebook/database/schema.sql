CREATE DATABASE db_bluebook;
use db_bluebook;

CREATE TABLE IF NOT EXISTS tb_leitores (
    lei_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    lei_nome TEXT NOT NULL,
    lei_email TEXT NOT NULL,
    lei_telefone VARCHAR(200) NOT NULL,
    lei_endereço VARCHAR(200) NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_users (
    use_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    use_nome TEXT NOT NULL,
    use_senha TEXT NOT NULL,
    use_tipo TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_books (
    boo_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    boo_titulo TEXT NOT NULL,
    boo_autor TEXT NOT NULL,
    boo_genero TEXT NOT NULL,
    boo_isbn VARCHAR(90) NOT NULL,
    boo_quant_estoque INT NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_lending(
    len_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    len_data_emprestimo DATE NOT NULL,
    len_data_devolucao DATE NOT NULL,
    len_valor FLOAT,
    len_boo_id INT NOT NULL,
    len_use_id INT NOT NULL,
    
	FOREIGN KEY (len_boo_id) REFERENCES tb_books(boo_id),
    FOREIGN KEY (len_use_id) REFERENCES tb_users(use_id)
);
