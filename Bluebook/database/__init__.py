import mysql.connector as sql

def obter_conexao():
    db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'db_Bluebook'
    }
    conn = sql.connect(**db_config, auth_plugin='mysql_native_password')
    
    return conn