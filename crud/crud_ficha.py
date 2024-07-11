import json
from models.Ficha_Medica import FichaMedica as fic
from db_conection import connect

def create_ficha(ficha_medica):
    try:
        conn = connect()
        cursor = conn.cursor()
        query = ("""
            INSERT INTO ficha_medica (
                pac_rut,
                pac_nombre,
                pac_apellido,
                
        """)
        valores = (fic.ficha_id, fic.pac_rut, fic.pac_nombre, fic.pac_apellido, fic.med_nombre, fic.med_apellido, fic.esp_nombre, fic.his_detalle, fic.exam_nombre, fic.pac_diagnos, fic.fecha_atencion)
        cursor.execute(query, valores)
        conn.commit()
        print('Ficha médica creada con éxito.')
        create_json_ficha(ficha_medica)
    except:
        print('Error al crear la ficha médica.')

def create_json_ficha(ficha_medica):
    ficha_dict = {
        "id": ficha_medica.ficha_id,
        "nombre_paciente": ficha_medica.pac_nombre,
        "medico_id": ficha_medica.medico_id,
        "nombre_medico": ficha_medica.med_nombre,
        "especialidad": ficha_medica.esp_nombre,
        "descripcion": ficha_medica.pac_diagnos,
        "fecha": str(ficha_medica.fecha_atencion)
    }
    with open(f"ficha_medica/{ficha_medica.ficha_id}.json", "r") as file:
        json.dump(ficha_dict, file, indent=4)

def read_ficha():
    try:
        conn = connect()
        cursor = conn.cursor()
        query = ("""
            SELECT 
                f.ficha_id, 
                f.pac_nombre,  
                f.med_rut, 
                m.med_nombre AS nombre_medico, 
                e.esp_nombre AS especialidad, 
                f.pac_diagnos, 
                f.fecha_atencion
            FROM ficha_medicas f
            WHERE f.ficha_id = %s
            JOIN medicos m ON f.med_rut = m.med_rut
            JOIN especialidades e ON m.especialidad_id = e.id
        """)
        valores = (fic.ficha_id)
        cursor.execute(query, valores)
        conn.commit()
        cursor.close()
        conn.close()
    except:
        print('Error al encontrar la ficha.')