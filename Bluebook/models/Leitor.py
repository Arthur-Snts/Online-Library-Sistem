from database import obter_conexao

class Leitor():
    

    @classmethod
    def all(cls):
        conn = obter_conexao()  
        cursor = conn.cursor(dictionary=True)

        cursor.execute('SELECT * FROM tb_leitores')
        consulta_usuarios = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()

        return consulta_usuarios
    
    @classmethod
    def cadastro(cls, nome, email, telefone, endereco):
        conn = obter_conexao()  
        cursor = conn.cursor()      
        cursor.execute("INSERT INTO tb_leitores (lei_nome, lei_email, lei_telefone, lei_endereco) VALUES (%s, %s, %s, %s)", (nome, email, telefone, endereco))
        conn.commit()
        conn.close()
    
    @classmethod
    def listar(cls, order_by):
        conn = obter_conexao()  
        cursor = conn.cursor(dictionary=True)
        query = f'SELECT * FROM tb_leitores ORDER BY lei_nome {order_by}'
        cursor.execute(query)
        leitores = cursor.fetchall()
        cursor.close()
        conn.close()
        return leitores
    @classmethod
    def one(cls, id):
        conn = obter_conexao()  
        cursor = conn.cursor(dictionary=True)
        query = f'SELECT * FROM tb_leitores where lei_id = {id}'
        cursor.execute(query)
        leitor = cursor.fetchone()
        cursor.close()
        conn.close()
        return leitor
    @classmethod
    def delete(cls,id):
        conn = obter_conexao()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tb_leitores WHERE lei_id = %s', (id,))
        conn.commit()
        cursor.close()
        conn.close()
    @classmethod
    def update(cls, id, nome, email, telefone, endereco):
        conn = obter_conexao()
        cursor = conn.cursor()

        query = 'UPDATE tb_leitores SET lei_nome = %s, lei_email = %s, lei_telefone = %s, lei_endereco = %s WHERE lei_id = %s'
        cursor.execute(query, (nome, email, telefone, endereco,id))
        conn.commit()
        cursor.close()
        conn.close()