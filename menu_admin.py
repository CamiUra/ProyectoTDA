from ADMIN import Admin as ad

class Menu_Admin:
    def menu():
        print('-- Menú de Administrador --')
        while True:
            print('''
                1.- Administrar médicos
                2.- Administrar bodega
                3.- Administrar exámenes
                4.- Administrar especialidades
                5.- Salir
            ''')
            opcion = input('>>> ')
            if opcion == '1':
                print('''-- Seleccione una opcion --
                    1.- Crear usuario médico
                    2.- Ver usuarios médicos
                    3.- Modificar usuario médico
                    4.- Eliminar usuario médico
                    5.- Volver atrás
                ''')
            elif opcion == "2":
                print('''-- Seleccione una opcion --
                    1.- Agregar producto
                    2.- Ver productos
                    3.- Modificar stock
                    4.- Eliminar producto
                    5.- Volver atrás
                    ''')
            elif opcion == "3":
                print('''-- Seleccione una opcion -- 
                    1.- Crear un examen
                    2.- Ver examenes
                    3.- Modificar un examen
                    4.- Eliminar examen
                    5.- Volver atrás''')
                
        else:
            print('Error inesperado')

Menu_Admin.menu()