# Importando o conector MySQL
import mysql.connector

db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': ''
}

try:
    # Tentando estabelecer uma conexão
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    print("Conexão estabelecida com sucesso.")
    
    # Localização do SQL
    SCHEMA = "database/schema.sql"

    # Declara o SQL para o banco
    with open(SCHEMA, 'r') as f:
        sql_script = f.read()

    # Executa cada statement do script SQL
    for statement in sql_script.split(';'):
        if statement.strip():  # Evita statements vazios
            try:
                cursor.execute(statement)
            except mysql.connector.Error as e:
                print(f"Erro ao executar statement: {e}")

    # Commit das operações
    conn.commit()
    print("Script executado com sucesso.")

except mysql.connector.Error as erro:
    print(f"Erro ao conectar ou executar operações no banco de dados: {erro}")

finally:
    # Garante que cursor e conexão serão fechados
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()