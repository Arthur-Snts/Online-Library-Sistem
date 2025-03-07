from database import obter_conexao

class Lending():
    

    @classmethod
    def cadastro(cls, usuario, livro, devolucao, valor, user):
        conn = obter_conexao()  
        cursor = conn.cursor(dictionary=True)
        cursor.execute("INSERT INTO tb_lending (len_data_devolucao,  len_valor, len_lei_id, len_boo_id, len_use_id) VALUES ((curdate() + interval %s day),%s, %s, %s, %s)", ( devolucao, valor,usuario, livro, user ))
        conn.commit()
        conn.close()

    @classmethod
    def listar(cls, order_by):
        conn = obter_conexao()  
        cursor = conn.cursor(dictionary=True)
        query = f'SELECT * FROM tb_lending join tb_leitores on lei_id = len_lei_id join tb_books on boo_id = len_boo_id ORDER BY len_data_emprestimo {order_by}'
        cursor.execute(query)
        emprestimos = cursor.fetchall()
        cursor.close()
        conn.close()

        return emprestimos
    
    @classmethod
    def all(cls):
        conn = obter_conexao()  
        cursor = conn.cursor(dictionary=True)

        cursor.execute('SELECT * FROM tb_lending join tb_leitores on lei_id = len_lei_id join tb_books on boo_id = len_boo_id')
        consulta_emprestimos = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()

        return consulta_emprestimos
    
    @classmethod
    def delete(cls,id):
        conn = obter_conexao()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tb_lending WHERE len_id = %s', (id,))
        conn.commit()
        cursor.close()
        conn.close()
    
    @classmethod
    def update(cls, leitor, livro, devolucao, valor, user, id):
        conn = obter_conexao()
        cursor = conn.cursor()

        query = 'UPDATE tb_lending SET len_lei_id = %s, len_boo_id = %s, len_data_devolucao = %s, len_valor = %s, len_use_id = %s WHERE len_id = %s'
        cursor.execute(query, (leitor, livro, devolucao, valor, user, id))
        conn.commit()
        cursor.close()
        conn.close()

    @classmethod
    def one(cls, id):
        conn = obter_conexao()  
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f'SELECT * FROM tb_lending join tb_leitores on lei_id = len_lei_id join tb_books on boo_id = len_boo_id where len_id = {id}')
        emp = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return emp