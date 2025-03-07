import mysql.connector

db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': ''
}

try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    with open("database/schema.sql", "r") as f:
        sql_script = f.read()

    # Executando comandos individualmente para capturar saídas
    for statement in sql_script.split(";"):
        statement = statement.strip()
        if statement:
            try:
                print(f"Executando: {statement[:100]}...")  # Mostra os primeiros 100 caracteres
                cursor.execute(statement)
            except mysql.connector.Error as e:
                print(f"Erro ao executar: {e}")

    conn.commit()
    print("Script executado com sucesso.")

except mysql.connector.Error as erro:
    print(f"Erro no banco de dados: {erro}")

finally:
    cursor.close()
    conn.close()