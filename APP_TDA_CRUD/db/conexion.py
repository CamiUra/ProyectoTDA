import mysql.connector
from mysql.connector import Error

class DAO():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '',
                db= 'kcv'
                )
        except Error as err:
            print('Error al conectar: {0}'.format(err))

    def get_conn(self):
        return self.conexion
    
    def get_cursor(self):
        try:
            return self.conexion.cursor()
        except AttributeError:
            print('Reconectando...')
            self.__init__()
            return self.conexion.cursor()
    
    def close(self):
        if self.conexion:
            self.conexion.close()
    
