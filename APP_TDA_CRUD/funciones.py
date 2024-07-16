import json
usuarios_medicos = 'medicos.json'
from db.conexion import DAO
import mysql.connector

dao = DAO()

#Funciones JSON

def inicializar_json():
    try:
        with open('medicos.json', 'r') as archivo:
            pass
    except FileNotFoundError:
        with open('medicos.json', 'w') as archivo:
            json.dump({}, archivo)

def guardar_usuario_medico_en_json(rut_medico, clave):
    try:
        with open("usuarios_medicos.json", "r") as archivo:
            usuarios = json.load(archivo)
    except FileNotFoundError:
        usuarios = {}

    usuarios[rut_medico] = clave

    with open("usuarios_medicos.json", "w") as archivo:
        json.dump(usuarios, archivo)


#Funciones CRUD Médico

def crear_usuario_medico(rut_medico, nombre_medico, apellido_medico, id_especialidad):
    connection = dao.get_conn()
    cursor = dao.get_cursor()
    clave = "corona" + rut_medico[:4]
    try:
        cursor.execute("INSERT INTO medicos (rut_medico, nombre_medico, apellido_medico, id_especialidad) VALUES (%s, %s, %s, %s)",
                       (rut_medico, nombre_medico, apellido_medico, id_especialidad))
        connection.commit()
        guardar_usuario_medico_en_json(rut_medico, clave)
        print(f"Médico {nombre_medico} {apellido_medico} creado correctamente")
    except mysql.connector.Error as err:
        print(f"Error al crear médico: {err}")
    finally:
        cursor.close()

def leer_usuarios_medicos():
    connection = dao.get_conn()
    cursor = dao.get_cursor()
    try:
        cursor.execute("SELECT * FROM medicos")
        medicos = cursor.fetchall()
        if medicos:
            for medico in medicos:
                print(medico)
        else:
            print("No hay médicos disponibles")
    except mysql.connector.Error as err:
        print(f"Error al leer médicos: {err}")
    finally:
        cursor.close()
        connection.close()

def actualizar_usuario_medico(rut_medico, nuevo_nombre=None, nuevo_apellido=None, nueva_especialidad=None):
    connection = dao.get_conn()
    cursor = dao.get_cursor()
    try:
        if nuevo_nombre:
            cursor.execute("UPDATE medicos SET nombre_medico = %s WHERE rut_medico = %s", (nuevo_nombre, rut_medico))
        if nuevo_apellido:
            cursor.execute("UPDATE medicos SET apellido_medico = %s WHERE rut_medico = %s", (nuevo_apellido, rut_medico))
        if nueva_especialidad:
            cursor.execute("UPDATE medicos SET id_especialidad = %s WHERE rut_medico = %s", (nueva_especialidad, rut_medico))
        
        connection.commit()
        print(f"Usuario {rut_medico} actualizado")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def eliminar_usuario_medico(rut_medico):
    connection = dao.get_conn()
    cursor = dao.get_cursor()
    try:
        cursor.execute("DELETE FROM medicos WHERE rut_medico = %s", (rut_medico,))
        connection.commit()
        
        with open('usuarios_medicos.json', 'r') as archivo:
            usuarios_medicos = json.load(archivo)
        
        if rut_medico in usuarios_medicos:
            del usuarios_medicos[rut_medico]
        
        with open('usuarios_medicos.json', 'w') as archivo:
            json.dump(usuarios_medicos, archivo)
        
        print(f"Usuario {rut_medico} eliminado")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

#Funciones CRUD Especialidad

def crear_especialidad(id_especialidad, nombre_especialidad):
    connection = dao.get_conn()
    cursor = dao.get_cursor()
    try:
        cursor.execute("INSERT INTO especialidades (id_especialidad, nombre_especialidad) VALUES (%s, %s)",
                       (id_especialidad, nombre_especialidad))
        connection.commit()
        print(f"Especialidad {nombre_especialidad} creada con ID {id_especialidad}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def leer_especialidades():
    connection = dao.get_conn()
    cursor = dao.get_cursor()
    try:
        cursor.execute("SELECT * FROM especialidades")
        especialidades = cursor.fetchall()
        if especialidades:
            for especialidad in especialidades:
                print(especialidad)
        else:
            print("No hay especialidades disponibles")
    except mysql.connector.Error as err:
        print(f"Error al leer especialidades: {err}")
    finally:
        cursor.close()

def actualizar_especialidad(id_especialidad, nuevo_nombre):
    connection = dao.get_conn()
    cursor = dao.get_cursor()
    try:
        cursor.execute("UPDATE especialidades SET nombre_especialidad = %s WHERE id_especialidad = %s",
                       (nuevo_nombre, id_especialidad))
        connection.commit()
        print(f"Especialidad {id_especialidad} actualizada a {nuevo_nombre}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def eliminar_especialidad(id_especialidad):
    connection = dao.get_conn()
    cursor = dao.get_cursor()
    try:
        cursor.execute("DELETE FROM especialidades WHERE id_especialidad = %s", (id_especialidad,))
        connection.commit()
        print(f"Especialidad {id_especialidad} eliminada")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

#Funciones CRUD Examen

def crear_examen(id_examen, nombre_examen, precio_examen):
    connection = dao.get_conn()
    cursor = dao.get_cursor()
    try:
        cursor.execute("INSERT INTO examenes (id_examen, nombre_examen, precio_examen) VALUES (%s, %s, %s)",
                       (id_examen, nombre_examen, precio_examen))
        connection.commit()
        print(f"Examen {nombre_examen} creado correctamente")
    except mysql.connector.Error as err:
        print(f"Error al crear examen: {err}")
    finally:
        cursor.close()

def leer_examenes():
    connection = dao.get_conn()
    cursor = dao.get_cursor()
    try:
        cursor.execute("SELECT * FROM examenes")
        examenes = cursor.fetchall()
        if examenes:
            for examen in examenes:
                print(examen)
        else:
            print("No hay exámenes disponibles")
    except mysql.connector.Error as err:
        print(f"Error al leer exámenes: {err}")
    finally:
        cursor.close()

def actualizar_examen(id_examen, nuevo_nombre=None, nuevo_precio=None):
    connection = dao.get_conn()
    cursor = dao.get_cursor()
    try:
        if nuevo_nombre:
            cursor.execute("UPDATE examenes SET nombre_examen = %s WHERE id_examen = %s", (nuevo_nombre, id_examen))
        if nuevo_precio:
            cursor.execute("UPDATE examenes SET precio_examen = %s WHERE id_examen = %s", (nuevo_precio, id_examen))
        connection.commit()
        print(f"Examen {id_examen} actualizado correctamente")
    except mysql.connector.Error as err:
        print(f"Error al actualizar examen: {err}")
    finally:
        cursor.close()

def eliminar_examen(id_examen):
    connection = dao.get_conn()
    cursor = dao.get_cursor()
    try:
        cursor.execute("DELETE FROM examenes WHERE id_examen = %s", (id_examen,))
        connection.commit()
        print(f"Examen {id_examen} eliminado correctamente")
    except mysql.connector.Error as err:
        print(f"Error al eliminar examen: {err}")
    finally:
        cursor.close()

#Funciones CRUD Producto

def crear_producto(id_producto, nombre_producto, cantidad, precio_producto):
    connection = dao.get_conn()
    cursor = dao.get_cursor()
    try:
        cursor.execute("INSERT INTO productos (id_producto, nombre_producto, cantidad, precio_producto) VALUES (%s, %s, %s, %s)",
                       (id_producto, nombre_producto, cantidad, precio_producto))
        connection.commit()
        print(f"Producto {nombre_producto} creado correctamente")
    except mysql.connector.Error as err:
        print(f"Error al crear producto: {err}")
    finally:
        cursor.close()

def leer_productos():
    connection = dao.get_conn()
    cursor = dao.get_cursor()
    try:
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        if productos:
            for producto in productos:
                print(producto)
        else:
            print("No hay productos disponibles")
    except mysql.connector.Error as err:
        print(f"Error al leer productos: {err}")
    finally:
        cursor.close()

def actualizar_producto(id_producto, nuevo_nombre=None, nueva_cantidad=None, nuevo_precio=None):
    connection = dao.get_conn()
    cursor = dao.get_cursor()
    try:
        if nuevo_nombre:
            cursor.execute("UPDATE productos SET nombre_producto = %s WHERE id_producto = %s", (nuevo_nombre, id_producto))
        if nueva_cantidad:
            cursor.execute("UPDATE productos SET cantidad = %s WHERE id_producto = %s", (nueva_cantidad, id_producto))
        if nuevo_precio:
            cursor.execute("UPDATE productos SET precio_producto = %s WHERE id_producto = %s", (nuevo_precio, id_producto))
        connection.commit()
        print(f"Producto {id_producto} actualizado correctamente")
    except mysql.connector.Error as err:
        print(f"Error al actualizar producto: {err}")
    finally:
        cursor.close()

def eliminar_producto(id_producto):
    connection = dao.get_conn()
    cursor = dao.get_cursor()
    try:
        cursor.execute("DELETE FROM productos WHERE id_producto = %s", (id_producto,))
        connection.commit()
        print(f"Producto {id_producto} eliminado correctamente")
    except mysql.connector.Error as err:
        print(f"Error al eliminar producto: {err}")
    finally:
        cursor.close()