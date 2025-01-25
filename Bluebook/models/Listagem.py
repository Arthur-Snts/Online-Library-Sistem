from database import obter_conexao    


class Listagem():
    
    @classmethod
    def um(cls, use_id,data1, data2):
        conn = obter_conexao()  
        cursor = conn.cursor(dictionary=True)
        query = f"SELECT use_nome, sum(len_preco) as soma FROM tb_lending JOIN tb_users ON len_use_id = use_id WHERE use_id = {use_id} and (len_data_emprestimo between '{data1}' and '{data2}') "
        cursor.execute(query)
        total_emprestimos = cursor.fetchall()
        cursor.close()
        conn.close()
        return total_emprestimos
    @classmethod
    def dois(cls, data1, data2):
        conn = obter_conexao()  
        cursor = conn.cursor(dictionary=True)
        query = f"select use_nome, sum(len_preco) as soma from tb_lending join tb_users on len_use_id = use_id where len_data_emprestimo between '{data1}' and '{data2}' group by use_nome having sum(len_preco) > 100"
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