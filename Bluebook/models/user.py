from database import obter_conexao

class User():
    

    @classmethod
    def all(cls):
        conn = obter_conexao()  
        cursor = conn.cursor(dictionary=True)

        cursor.execute('SELECT * FROM tb_users')
        consulta_usuarios = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()

        return consulta_usuarios
    
    @classmethod
    def cadastro(cls, nome, email, telefone, endereco):
        conn = obter_conexao()  
        cursor = conn.cursor()      
        cursor.execute("INSERT INTO tb_users (use_nome, use_email, use_telefone, use_endereco) VALUES (%s, %s, %s, %s)", (nome, email, telefone, endereco))
        conn.commit()
        conn.close()
    
    @classmethod
    def listar(cls, order_by):
        conn = obter_conexao()  
        cursor = conn.cursor(dictionary=True)
        query = f'SELECT * FROM tb_users ORDER BY use_nome {order_by}'
        cursor.execute(query)
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return users
    @classmethod
    def one(cls, id):
        conn = obter_conexao()  
        cursor = conn.cursor(dictionary=True)
        query = f'SELECT * FROM tb_users where use_id = {id}'
        cursor.execute(query)
        user = cursor.fetchall()
        cursor.close()
        conn.close()
        return user
    @classmethod
    def delete(cls,id):
        conn = obter_conexao()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tb_users WHERE use_id = %s', (id,))
        conn.commit()
        cursor.close()
        conn.close()
    @classmethod
    def update(cls, id, nome, email, telefone, endereco):
        conn = obter_conexao()
        cursor = conn.cursor()

        query = 'UPDATE tb_users SET use_nome = %s, use_email = %s, use_telefone = %s, use_endereco = %s WHERE use_id = %s'
        cursor.execute(query, (nome, email, telefone, endereco,id))
        conn.commit()
        cursor.close()
        conn.close()