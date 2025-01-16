CREATE DATABASE db_bluebook;


CREATE TABLE IF NOT EXISTS tb_users (
    use_id INTEGER PRIMARY KEY AUTOINCREMENT,
    use_nome TEXT NOT NULL,
    use_email TEXT NOT NULL,
    use_telefone INT NOT NULL,
    use_endereço VARCHAR(90) NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_books (
    boo_id INTEGER PRIMARY KEY AUTOINCREMENT,
    boo_titulo TEXT NOT NULL,
    boo_autor TEXT NOT NULL,
    boo_genero TEXT NOT NULL,
    boo_isbn VARCHAR(90) NOT NULL,
    boo_quant_estoque INT NOT NULL,
    boo_use_id INTEGER NOT NULL,

    FOREIGN KEY(boo_use_id) REFERENCES tb_users(use_id)
);

CREATE TABLE IR NOT EXISTS tb_lending(
    len_id INTEGER PRIMARY KEY AUTOINCREMENT,
    len_data_emprestimo DATE NOT NULL,
    len_data_devolucao DATE NOT NULL,
    len_boo_id INT NOT NULL,
    len_use_id INT NOT NULL,

    FOREIGN KEY (len_boo_id) REFERENCES tb_books(boo_id),
    FOREIGN KEY (len_use_id) REFERENCES tb_users(use_id)
);