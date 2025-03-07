from database import obter_conexao    


class Listagem():
    
    @classmethod
    def um(cls, use_id,data1, data2):
        conn = obter_conexao()  
        cursor = conn.cursor(dictionary=True)
        query = "SELECT lei_nome, sum(len_valor) as soma FROM tb_lending JOIN tb_leitores ON len_lei_id = lei_id WHERE lei_id = %s and (len_data_emprestimo between %s and %s) "
        cursor.execute(query, (use_id, data1, data2,))
        total_emprestimos = cursor.fetchall()
        cursor.close()
        conn.close()
        return total_emprestimos
    @classmethod
    def dois(cls, data1, data2):
        conn = obter_conexao()  
        cursor = conn.cursor(dictionary=True)
        query = f"select lei_nome, sum(len_valor) as soma from tb_lending join tb_leitores on len_lei_id = lei_id where len_data_emprestimo between '{data1}' and '{data2}' group by lei_nome having sum(len_valor) > 100"
        cursor.execute(query)
        usuarios = cursor.fetchall()
        cursor.close()
        conn.close()
        return usuarios
    
    @classmethod
    def tres(cls, dias):
        conn = obter_conexao()  
        cursor = conn.cursor(dictionary=True)
        query = f"select boo_titulo, count(len_id) as qnt_emprestimos from tb_lending join tb_books on len_boo_id = boo_id where len_data_emprestimo >= curdate() - interval {dias} day group by boo_titulo order by qnt_emprestimos desc limit 10"
        cursor.execute(query)
        livros = cursor.fetchall()
        cursor.close()
        conn.close()
        return livros
    
    @classmethod
    def quatro(cls, dias):
        conn = obter_conexao()  
        cursor = conn.cursor(dictionary=True)
        query = f"select boo_titulo from tb_books where boo_id not in (select len_boo_id from tb_lending where len_data_emprestimo >= curdate() - interval {dias} day);"
        cursor.execute(query)
        livros = cursor.fetchall()
        cursor.close()
        conn.close()
        return livros
    
    @classmethod
    def logs(cls):
        conn = obter_conexao()  
        cursor = conn.cursor(dictionary=True)
        query = "select * from tb_logs join tb_leitores on log_lei_id = lei_id order by log_data_hora"
        cursor.execute(query)
        logs = cursor.fetchall()
        cursor.close()
        conn.close()
        return logs