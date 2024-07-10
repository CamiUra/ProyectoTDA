from db_conection import DBconn

class Admin:
    def __init__(self, adm_id):
        self.adm_id = adm_id

    def c_med(med_rut, med_nombre, med_apellido, esp_id):
        try:
            db = DBconn()
            cursor = db.conn.cursor()
            query = 'INSERT INTO medicos (med_rut, med_nombre, med_apellido, esp_id) VALUES (%s,%s,%s,%s)'
            valores = (med_rut, med_nombre, med_apellido, esp_id)
            cursor.execute(query, valores)
            db.conn.commit()
            print('Usuario médico creado.')
            cursor.close()
        except:
            print('Error al crear el usuario médico.')

    def r_med():
        try:
            db = DBconn()
            cursor = db.conn.cursor()
            query = 'SELECT * FROM medicos'
            cursor.execute(query)
            data = cursor.fetchall()
            print('--- Datos del Médico ---')
            for row in data:
                print(f'''RUT: {row[0]},
                      Nombre: {row[1]},
                      Apellido: {row[2]},
                      Especialidad: {row[3]}''')
                cursor.close()
        except:
            print('Error al mostrar los datos del médico.')

    def u_med(med_rut, med_nombre, med_apellido, esp_id):
        try:
            db = DBconn()
            cursor = db.conn.cursor()
            query = 'UPDATE medicos SET med_nombre = %s, med_apellido = %s, esp_id =%s WHERE rut_med = %s'
            valores = (med_nombre, med_apellido, esp_id, med_rut)
            cursor.execute(query, valores)
            db.conn.commit()
            print('Usuario médico actualizado.')
            cursor.close()
        except:
            print('Error al actualizar el usuario médico.')
    
    def d_med(med_rut):
        try:
            db = DBconn()
            cursor = db.conn.cursor()
            query = 'DELETE FROM medicos WHERE med_rut = %s'
            valores = (med_rut)
            cursor.execute(query, valores)
            db.conn.commit()
            print('Usuario médico eliminado.')
            cursor.close()
        except:
            print('Error al eliminar el usuario médico.')

    def c_bod(prod_id, prod_nombre, prod_cantidad):
        try:
            db = DBconn()
            cursor = db.conn.cursor()
            query = 'INSERT INTO bodega (prod_nombre, prod_cantidad) VALUES (%s,%s)'
            valores = (prod_nombre, prod_cantidad)
            cursor.execute(query, valores)
            db.conn.commit()
            print('Producto agregado a la bodega.')
            cursor.close()
        except:
            print('Error al agregar el producto a la bodega.')

    def r_bod():
        try:
            db = DBconn()
            cursor = db.conn.cursor()
            query = 'SELECT * FROM bodega'
            cursor.execute(query)
            data = cursor.fetchall()
            print('--- Bodega ---')
            for rows in data:
                print(f'''ID: {rows[0]},
                      Nombre Producto: {rows[1]},
                      Cantidad: {rows[2]}''')
                cursor.close()
        except:
            print('Error al mostrar la bodega.')

    def u_bod(prod_id, prod_cantidad):
        try:
            db = DBconn()
            cursor = db.conn.cursor()
            query = 'UPDATE bodega SET prod_cantidad = %s WHERE prod_id = %s'
            valores = (prod_cantidad, prod_id)
            cursor.execute(query, valores)
            db.conn.commit()
            print('Producto actualizado en la bodega.')
            cursor.close()
        except:
            print('Error al actualizar el producto en la bodega.')

    def d_bod(prod_id):
        try:
            db = DBconn()
            cursor = db.conn.cursor()
            query = 'DELETE FROM bodega WHERE prod_id = %s'
            valores = (prod_id)
            cursor.execute(query, valores)
            db.conn.commit()
            print('Producto eliminado de la bodega.')
            cursor.close()
        except:
            print('Error al eliminar el producto de la bodega.')

    def c_esp(esp_id, esp_nombre):
        try:
            db = DBconn()
            cursor = db.conn.cursor()
            query = 'INSERT INTO especialidad (esp_nombre) VALUES (%s)'
            valores = (esp_nombre)
            cursor.execute(query, valores)
            db.conn.commit()
            print('Especialidad creada.')
            cursor.close()
        except:
            print('Error al crear la especialidad.')

    def r_esp():
        try:
            db = DBconn()
            cursor = db.conn.cursor()
            query = 'SELECT * FROM especialidad'
            cursor.execute(query)
            data = cursor.fetchall()
            print('--- Especialidades ---')
            for rows in data:
                print(f'''ID: {rows[0]},
                      Nombre: {rows[1]}''')
                cursor.close()
        except:
            print('Error al mostrar las especialidades.')

    def u_esp(esp_id, esp_nombre):
        try:
            db = DBconn()
            cursor = db.conn.cursor()
            query = 'UPDATE especialidad SET esp_nombre = %s WHERE esp_id = %s'
            valores = (esp_nombre, esp_id)
            cursor.execute(query, valores)
            db.conn.commit()
            print('Especialidad actualizada.')
            cursor.close()
        except:
            print('Error al actualizar la especialidad.')

    def d_esp(esp_id):
        try:
            db = DBconn()
            cursor = db.conn.cursor()
            query = 'DELETE FROM especialidad WHERE esp_id = %s'
            valores = (esp_id)
            cursor.execute(query, valores)
            db.conn.commit()
            print('Especialidad eliminada.')
            cursor.close()
        except:
            print('Error al eliminar la especialidad.')

    def c_exam(exam_id, exam_nombre, exam_precio):
        try:
            db = DBconn()
            cursor = db.conn.cursor()
            query = 'INSERT INTO examenes (exam_nombre, exam_precio) VALUES (%s,%s)'
            valores = (exam_nombre, exam_precio)
            cursor.execute(query, valores)
            db.conn.commit()
            print('Examen creado.')
            cursor.close()
        except:
            print('Error al crear el examen.')

    def r_exam():
        try:
            db = DBconn()
            cursor = db.conn.cursor()
            query = 'SELECT * FROM examenes'
            cursor.execute(query)
            data = cursor.fetchall()
            print('--- Exámenes ---')
            for rows in data:
                print(f'''ID: {rows[0]},
                      Nombre: {rows[1]},
                      Precio: {rows[2]}''')
                cursor.close()
        except:
            print('Error al mostrar los exámenes.')

    def u_exam(exam_id, exam_nombre, exam_precio):
        try:
            db = DBconn()
            cursor = db.conn.cursor()
            query = 'UPDATE examenes SET exam_nombre = %s, exam_precio = %s WHERE exam_id = %s'
            valores = (exam_nombre, exam_precio, exam_id)
            cursor.execute(query, valores)
            db.conn.commit()
            print('Examen actualizado.')
            cursor.close()
        except:
            print('Error al actualizar el examen.')

    def d_exam(exam_id):
        try:
            db = DBconn()
            cursor = db.conn.cursor()
            query = 'DELETE FROM examenes WHERE exam_id = %s'
            valores = (exam_id,)
            cursor.execute(query, valores)
            db.conn.commit()
            print('Examen eliminado.')
            cursor.close()
        except:
            print('Error al eliminar el examen.')