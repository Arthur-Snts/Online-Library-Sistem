from database import obter_conexao
from flask_login import UserMixin

class User(UserMixin):
    id: str
    def __init__(self, nome, senha, tipo):
        self.nome = nome
        self.senha = senha
        self.tipo = tipo
    
    @classmethod
    def get(cls, id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        SELECT = 'SELECT * FROM tb_users WHERE use_id=%s'
        cursor.execute(SELECT, (id,))
        dados = cursor.fetchone()
        if dados:
            user = User(dados[1], dados[2], dados[3])
            user.id = dados[0]
        else: 
            user = None
        return user
    
    @classmethod
    def all(cls):
        conn = obter_conexao()
        cursor = conn.cursor()
        cursor.execute("SELECT * from tb_users")
        users = cursor.fetchall()
        conn.commit()
        conn.close()
        return users
    
    @classmethod
    def nome(cls, nome):
        conn = obter_conexao()
        cursor = conn.cursor()
        cursor.execute("SELECT * from tb_users WHERE use_nome=%s", (nome,))
        dados = cursor.fetchone()
        user = User(dados[1], dados[2], dados[3])
        user.id = dados[0]
        return user
    
    @classmethod
    def insert(cls, nome, tipo, senha):
        conn = obter_conexao()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tb_users (use_nome, use_senha, use_tipo) VALUES (%s, %s, %s)", (nome, senha, tipo ))
        conn.commit()
        conn.close()