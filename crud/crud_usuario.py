from models.USER import Usuario as u
from db_conection import connect

def c_user(usuario):
    conn = connect()
    cursor = conn.cursor()
    query = 'INSERT INTO usuarios (user_id, user_name, user_password) VALUES (%s,%s,%s)'
    valores = (u.user_id, u.user_name, u.user_password)
    cursor.execute(query, valores)
    conn.commit()
    cursor.close()
    conn.close()

def get_user(user_name):
    try:
        conn = connect()
        cursor = conn.cursor()
        query = 'SELECT * FROM usuarios WHERE user_name = %s', (u.user_name)
        cursor.execute(query)
        usuario = cursor.fetchone()
        print('--- Lista de Usuarios ---')
        cursor.close()
        conn.close()
        return u(*usuario) if usuario else None
    except:
        print('Error al mostrar la lista de usuarios.')