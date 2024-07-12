from models.MEDICO import Medico as m
from db_conection import connect

def c_med(medico):
        try:
            conn = connect()
            cursor = conn.cursor()
            query = 'INSERT INTO medicos (med_rut, med_nombre, med_apellido, esp_id) VALUES (%s,%s,%s, NULL)'
            valores = (m.med_rut, m.med_nombre, m.med_apellido)
            cursor.execute(query, valores)
            conn.commit()
            print('Usuario médico creado.')
            cursor.close()
            conn.close()    
        except:
            print('Error al crear el usuario médico.')

def r_med():
    try:
        conn = connect()
        cursor = conn.cursor()
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
        conn.close()
    except:
        print('Error al mostrar los datos del médico.')

def get_med(user_name):
     conn = connect()
     cursor = conn.cursor()
     query = 'SELECT * FROM medicos WHERE med_rut = %s'
     valores = (m.med_rut)
     cursor.execute(query,valores)
     medico = cursor.fetchone()
     cursor.close()
     conn.close()
     return m(*medico) if medico else None

def u_med(medico):
    try:
        conn = connect()
        cursor = conn.cursor()
        query = 'UPDATE medicos SET med_nombre = %s, med_apellido = %s, esp_id =%s WHERE rut_med = %s'
        valores = (m.med_nombre, m.med_apellido, m.esp_id, m.med_rut)
        cursor.execute(query, valores)
        conn.commit()
        print('Usuario médico actualizado.')
        cursor.close()
        conn.close()
    except:
            print('Error al actualizar el usuario médico.')
    
def d_med(medico):
    try:
        conn = connect()
        cursor = conn.cursor()
        query = 'DELETE FROM medicos WHERE med_rut = %s'
        valores = (m.med_rut)
        cursor.execute(query, valores)
        conn.commit()
        print('Usuario médico eliminado.')
        cursor.close()
    except:
        print('Error al eliminar el usuario médico.')