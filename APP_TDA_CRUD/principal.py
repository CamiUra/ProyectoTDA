from db.conexion import DAO
from funciones import *

dao = DAO()

def menuGeneral():
    print('')

def menuAdmin():
    inicializar_json()
    print('\nMenu administrador')
    while True:
        print('''\nSeleccione una opción:
            1.- Administrar medico
            2.- Administrar bodega
            3.- Administrar examenes
            4.- Administrar especialidades
            5.- Salir''')
        opcion = input('>>> ')
        if opcion == '1':
            while True:
                print('''Seleccione una opción:
                    1.- Crear médico
                    2.- Ver médicos
                    3.- Actualizar médico
                    4.- Eliminar médico
                    5.- Volver''')
                x = input('>>> ')
                if x == '1':
                    print('Ingrese los siguientes datos del médico:')
                    rut_medico = input('RUT: ')
                    nombre_medico = input('Nombre: ')
                    apellido_medico = input('Apellido: ')
                    id_especfialidad = input('ID de especialidad: ')
                    crear_usuario_medico(rut_medico, nombre_medico, apellido_medico, id_especfialidad)
                elif x == '2':
                    print('\nLista de médicos: ')
                    leer_usuarios_medicos()
                elif x == '3':
                    rut_medico = input('Ingrese el RUT del médico: ')
                    print('Ingrese los siguientes datos a modificar: ')
                    print('(Dejar en blanco los espacios que no se modificarán)')
                    nuevo_nombre = input('Nombre: ')
                    nuevo_apellido = input('Apellido: ')
                    nueva_especialidad = input('Id de especialidad: ')
                    actualizar_usuario_medico(rut_medico, nuevo_nombre if nuevo_nombre else None, nuevo_apellido if nuevo_apellido else None, nueva_especialidad if nueva_especialidad else None)
                elif x == '4':
                    print('Ingrese el RUT del médico a eliminar')
                    rut_medico = input('>>> ')
                    eliminar_usuario_medico(rut_medico)
                elif x == '5':
                    print('Volviendo al menú principal...')
                    break
                else:
                    print('Opcion inválida')
        elif opcion == '4':
            print('''\nSeleccione una opción:
                1.- Crear especialidad
                2.- Ver especialidades
                3.- Actualizar especialidad
                4.- Eliminar especialidad''')
            x = input('>>> ')
            if x == '1':
                print('Ingrese los siguientes datos de la especialidad: ')
                id_especfialidad = input('Asigne una ID: ')
                nombre_especialidad = input('Nombre de la especialidad: ')
                crear_especialidad(id_especfialidad, nombre_especialidad)
        elif opcion == '5':
            print('Cerrando la conexión...')
            dao.close()
            print('Saliendo del programa...')
            break
        else:
            print('Ingrese una opción válida...')


menuAdmin()