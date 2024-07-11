from auth import login
from utils import input_usuario, input_ficha_medica
from crud.crud_medico import leer_medicos
from crud.crud_ficha import create_ficha, read_ficha
from models.Ficha_Medica import FichaMedica

def menu_principal():
    while True:
        username, password = input_usuario()
        usuario = login(username, password)
        if usuario:
            if usuario["rol"] == "admin":
                menu_admin()
            else:
                menu_medico(usuario["usuario"])
        else:
            print("Credenciales incorrectas, intente nuevamente.")

def menu_medico(medico):
    while True:
        print("\nMenú Médico")
        print("1. Crear ficha médica")
        print("2. Ver pacientes atendidos")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            id, nombre_paciente, telefono_paciente, correo_paciente, medico_id, descripcion, fecha = input_ficha_medica()
            ficha_medica = FichaMedica(id, nombre_paciente, telefono_paciente, correo_paciente, medico_id, medico.nombre, medico.especialidad_id, descripcion, fecha)
            create_ficha(ficha_medica)
        elif opcion == '2':
            fichas = read_ficha()
            for ficha in fichas:
                if ficha.medico_id == medico.id:
                    print(f"ID: {ficha.id}, Paciente: {ficha.nombre_paciente}, Teléfono: {ficha.telefono_paciente}, Correo: {ficha.correo_paciente}, Médico: {ficha.nombre_medico}, Especialidad: {ficha.especialidad}, Descripción: {ficha.descripcion}, Fecha: {ficha.fecha}")
        elif opcion == '3':
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

def menu_admin():
    while True:
        print("\nMenú Administrador")
        print("1. CRUD Médicos")
        print("2. CRUD Bodega")
        print("3. CRUD Exámenes")
        print("4. CRUD Especialidades")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            # Llamar al menú CRUD de médicos
            pass
        elif opcion == '2':
            # Llamar al menú CRUD de bodega
            pass
        elif opcion == '3':
            # Llamar al menú CRUD de exámenes
            pass
        elif opcion == '4':
            # Llamar al menú CRUD de especialidades
            pass
        elif opcion == '5':
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
