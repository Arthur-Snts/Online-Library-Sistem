from database import obter_conexao

class Book():

    @classmethod
    def cadastro(cls, titulo, autor, genero, isbn, quant_estoque):

        conn = obter_conexao()  
        cursor = conn.cursor()      
        cursor.execute("INSERT INTO tb_books (boo_titulo, boo_autor, boo_genero, boo_isbn, boo_quant_estoque) VALUES (%s, %s, %s, %s, %s)", (titulo, autor,genero, isbn, quant_estoque ))
        conn.commit()
        conn.close()

    @classmethod
    def listar(cls, order_by):

        conn = obter_conexao()  
        cursor = conn.cursor(dictionary=True)
        query = f'SELECT * FROM tb_books ORDER BY boo_titulo {order_by}'
        cursor.execute(query)
        books = cursor.fetchall()
        cursor.close()
        conn.close()
        return books
    
    @classmethod
    def all(cls):
        conn = obter_conexao()  
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM tb_books')
        consulta_livros = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return consulta_livros
    @classmethod
    def one(cls, id):
        conn = obter_conexao()  
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f'SELECT * FROM tb_books where boo_id = {id}')
        consulta_livros = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return consulta_livros
    
    @classmethod
    def delete(cls,id):
        conn = obter_conexao()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tb_books WHERE boo_id = %s', (id,))
        conn.commit()
        cursor.close()
        conn.close()
    @classmethod
    def update(cls, id, titulo, autor, genero, isbn, quant_estoque):
        conn = obter_conexao()
        cursor = conn.cursor()

        query = 'UPDATE tb_books SET boo_titulo = %s, boo_autor = %s, boo_genero = %s, boo_isbn = %s, boo_quant_estoque = %s WHERE boo_id = %s'
        cursor.execute(query, (titulo,autor,genero,isbn,quant_estoque,id))
        conn.commit()
        cursor.close()
        conn.close()