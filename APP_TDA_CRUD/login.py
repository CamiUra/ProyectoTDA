import json
from db.conexion import DAO

dao = DAO()

def verificar_credenciales(usuario, clave):
    if usuario == "ADMIN" and clave == "admin123":
        return "Administrador"

    connection = dao.get_conn()
    cursor = dao.get_cursor()
    try:
        cursor.execute("SELECT rut_medico FROM medicos WHERE rut_medico = %s", (usuario,))
        resultado = cursor.fetchone()
        
        if resultado:
            with open('usuarios_medicos.json', 'r') as archivo:
                usuarios_medicos = json.load(archivo)
            
            if usuario in usuarios_medicos and usuarios_medicos[usuario] == clave:
                return "Médico"
    finally:
        cursor.close()
        connection.close()
    
    return None