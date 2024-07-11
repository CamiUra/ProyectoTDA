def input_login():
    username = input("Ingrese su nombre de usuario (RUT o 'ADMIN'): ")
    password = input("Ingrese su contraseña: ")
    return username, password

def input_ficha_medica():
    rut_paciente = input('Ingrese el rut del paciente: ')
    nombre_paciente = input("Ingrese el nombre del paciente: ")
    descripcion = input("Ingrese el diagnostico: ")
    fecha = input("Ingrese la fecha (DD-MM-YYYY): ")
    return rut_paciente, nombre_paciente, descripcion, fecha
