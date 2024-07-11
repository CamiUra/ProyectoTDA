from db_conection import connect

def c_esp(esp_id, esp_nombre):
    try:
        conn = connect()
        cursor = conn.cursor()
        query = 'INSERT INTO especialidad (esp_nombre) VALUES (%s)'
        valores = (esp_nombre)
        cursor.execute(query, valores)
        conn.commit()
        print('Especialidad creada.')
        cursor.close()
        conn.close()
    except:
        print('Error al crear la especialidad.')

def r_esp():
    try:
        conn = connect()
        cursor = conn.cursor()
        query = 'SELECT * FROM especialidad'
        cursor.execute(query)
        data = cursor.fetchall()
        print('--- Especialidades ---')
        for rows in data:
            print(f'''ID: {rows[0]},
                Nombre: {rows[1]}''')
            cursor.close()
            conn.close()
    except:
        print('Error al mostrar las especialidades.')

def u_esp(esp_id, esp_nombre):
    try:
        conn = connect()
        cursor = conn.cursor()
        query = 'UPDATE especialidad SET esp_nombre = %s WHERE esp_id = %s'
        valores = (esp_nombre, esp_id)
        cursor.execute(query, valores)
        conn.commit()
        print('Especialidad actualizada.')
        cursor.close()
        conn.close()
    except:
        print('Error al actualizar la especialidad.')

def d_esp(esp_id):
    try:
        conn = connect()
        cursor = conn.cursor()
        query = 'DELETE FROM especialidad WHERE esp_id = %s'
        valores = (esp_id)
        cursor.execute(query, valores)
        conn.commit()
        print('Especialidad eliminada.')
        cursor.close()
        conn.close()
    except:
        print('Error al eliminar la especialidad.')