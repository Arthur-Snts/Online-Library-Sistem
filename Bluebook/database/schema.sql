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
    len_devolvido BOOLEAN NOT NULL,
    len_valor DECIMAL(10, 2),
    len_boo_id INT NOT NULL,
    len_use_id INT NOT NULL,
    
	FOREIGN KEY (len_boo_id) REFERENCES tb_books(boo_id),
    FOREIGN KEY (len_use_id) REFERENCES tb_users(use_id)
);

CREATE TABLE IF NOT EXISTS tb_logs(
	log_id INTEGER PRIMARY KEY AUTO_INCREMENT,
	log_operacao VARCHAR(20) NOT NULL,
	log_len_id INT NOT NULL,
	log_usu_id INT NOT NULL,
	log_usuario TEXT NOT NULL,
	log_data_hora DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (log_len_id) REFERENCES tb_lending(len_id),
    FOREIGN KEY (log_usu_id) REFERENCES tb_users(use_id)
);

#criação da função que calcula valor da multa
DELIMITER //

CREATE FUNCTION calcular_multa(id_livro INT) RETURNS DECIMAL(10, 2)
BEGIN 
    DECLARE valor_emprestimo DECIMAL(10, 2);
    DECLARE data_ultrapassada DATE;
    DECLARE data_devolucao DATE;
    DECLARE quantidade_dias INT;
    DECLARE valor_multa DECIMAL(10, 2);
    
    SELECT len_data_devolucao INTO data_devolucao FROM tb_lending WHERE len_boo_id = id_livro;
    SELECT len_valor INTO valor_emprestimo FROM tb_lending WHERE len_boo_id = id_livro;
    
    SET data_ultrapassada = CURDATE();
     
    SET quantidade_dias = DATEDIFF(data_ultrapassada, data_devolucao);
    
    IF quantidade_dias <= 0 THEN
        RETURN 0.0;
    END IF;
    
    SET valor_multa = quantidade_dias * valor_emprestimo;
    RETURN valor_multa;
END //

DELIMITER ;
