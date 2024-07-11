from db_conection import connect

def c_exam(exam_id, exam_nombre, exam_precio):
    try:
        conn = connect()
        cursor = conn.cursor()
        query = 'INSERT INTO examenes (exam_nombre, exam_precio) VALUES (%s,%s)'
        valores = (exam_nombre, exam_precio)
        cursor.execute(query, valores)
        conn.commit()
        print('Examen creado.')
        cursor.close()
        conn.close()
    except:
        print('Error al crear el examen.')

def r_exam():
    try:
        conn = connect()
        cursor = conn.cursor()
        query = 'SELECT * FROM examenes'
        cursor.execute(query)
        data = cursor.fetchall()
        print('--- Exámenes ---')
        for rows in data:
            print(f'''ID: {rows[0]},
                    Nombre: {rows[1]},
                    Precio: {rows[2]}''')
            cursor.close()
            conn.close()
    except:
        print('Error al mostrar los exámenes.')

def u_exam(exam_id, exam_nombre, exam_precio):
    try:
        conn = connect()
        cursor = conn.cursor()
        query = 'UPDATE examenes SET exam_nombre = %s, exam_precio = %s WHERE exam_id = %s'
        valores = (exam_nombre, exam_precio, exam_id)
        cursor.execute(query, valores)
        conn.commit()
        print('Examen actualizado.')
        cursor.close()
        conn.close()
    except:
        print('Error al actualizar el examen.')

def d_exam(exam_id):
    try:
        conn = connect()
        cursor = conn.cursor()
        query = 'DELETE FROM examenes WHERE exam_id = %s'
        valores = (exam_id,)
        cursor.execute(query, valores)
        conn.commit()
        print('Examen eliminado.')
        cursor.close()
        conn.close()
    except:
        print('Error al eliminar el examen.')