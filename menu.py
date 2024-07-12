from auth import login
from crud.crud_medico import c_med, r_med, u_med, d_med, get_med
from crud.crud_ficha import create_ficha, read_ficha
from models.Ficha_Medica import FichaMedica
from models.MEDICO import Medico

def menu_principal():
    while True:
        username = input('Ingrese su usuario: ')
        password = input('Ingrese su clave: ')
        usuario = login(username, password)
        if usuario:
            if username == "ADMIN" and password == 'admincorona123':
                menu_admin()
            else:
                menu_medico(usuario[r_med(1)])
        else:
            print("Credenciales incorrectas, intente nuevamente.")

def menu_medico(medico):
    print("\nMenú Médico")
    while True:
        print('\nSeleccione una opción: ')
        print("1. Crear ficha médica")
        print("2. Ver pacientes atendidos")
        print("3. Salir")
        
        opcion = input('>>> ')
        
        if opcion == '1':
            print('')
        elif opcion == '2':
            print('')
        elif opcion == '3':
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

def menu_admin():
    while True:
        print('''\nMenú Administrador
            1. Administrar Médicos
            2. Administrar Bodega
            3. Administrar Exámenes
            4. Administrar Especialidades
            5. Salir
        ''')
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            print('''\nSeleccione una opcion
                    1.- Crear usuario médico
                    2.- Ver usuarios médicos
                    3.- Modificar usuario médico
                    4.- Eliminar usuario médico
                    5.- Volver atrás
                ''')
            x = input('>>> ')
            if x == '1':
                print('\nIngrese los siguiente datos del médico: ')
                Medico.med_rut = input('RUT: ')
                Medico.med_nombre = input('Nombre: ')
                Medico.med_apellido = input('Apellido: ')
                datos = (Medico.med_rut, Medico.med_nombre, Medico.med_apellido)
                c_med(datos)
        elif opcion == '2':
            print('''\nSeleccione una opcion
                    1.- Agregar producto
                    2.- Ver productos
                    3.- Modificar stock
                    4.- Eliminar producto
                    5.- Volver atrás
                ''')
        elif opcion == '3':
            print('''\nSeleccione una opcion
                    1.- Crear un examen
                    2.- Ver examenes
                    3.- Modificar un examen
                    4.- Eliminar examen
                    5.- Volver atrás
                ''')
        elif opcion == '4':
            print('''\nSeleccione una opcion 
                    1.- Crear una especialidad
                    2.- Ver especialidades
                    3.- Modificar una especialidad
                    4.- Eliminar una especialidad
                    5.- Volver atrás
                ''')
        elif opcion == '5':
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
