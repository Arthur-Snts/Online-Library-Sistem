CREATE DATABASE db_bluebook;
USE db_bluebook;


CREATE TABLE IF NOT EXISTS tb_users (
    use_id INTEGER PRIMARY KEY auto_increment,
    use_nome TEXT NOT NULL,
    use_email TEXT NOT NULL,
    use_telefone VARCHAR(200) NOT NULL,
    use_endereco VARCHAR(200) NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_books (
    boo_id INTEGER PRIMARY KEY auto_increment,
    boo_titulo TEXT NOT NULL,
    boo_autor TEXT NOT NULL,
    boo_genero TEXT NOT NULL,
    boo_isbn VARCHAR(90) NOT NULL,
    boo_quant_estoque INT NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_lending(
    len_id INTEGER PRIMARY KEY auto_increment,
    len_data_emprestimo DATE DEFAULT(CURDATE()) NOT NULL,
    len_data_devolucao DATE NOT NULL,
    len_preco FLOAT NOT NULL,
    len_boo_id INTEGER NOT NULL,
    len_use_id INTEGER NOT NULL,

    FOREIGN KEY (len_boo_id) REFERENCES tb_books(boo_id),
    FOREIGN KEY (len_use_id) REFERENCES tb_users(use_id)
);
