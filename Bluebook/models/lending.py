from database import obter_conexao

class Lending():
    

    @classmethod
    def cadastro(cls, usuario, livro, devolucao, valor):
        conn = obter_conexao()  
        cursor = conn.cursor(dictionary=True)
        cursor.execute("INSERT INTO tb_lending (len_data_devolucao,  len_preco, len_use_id, len_boo_id) VALUES ((curdate() + interval %s day),%s, %s, %s)", ( devolucao, valor,usuario, livro ))
        teste = cursor.fetchone()
        conn.commit()
        conn.close()

    @classmethod
    def listar(cls, order_by):
        conn = obter_conexao()  
        cursor = conn.cursor(dictionary=True)
        query = f'SELECT * FROM tb_lending join tb_users on use_id = len_use_id join tb_books on boo_id = len_boo_id ORDER BY len_data_emprestimo {order_by}'
        cursor.execute(query)
        emprestimos = cursor.fetchall()
        cursor.close()
        conn.close()

        return emprestimos