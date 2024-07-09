import mysql.connector

class DBconn:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conex = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host, 
                user=self.user, 
                password=self.password,
                database=self.database
            )
            print('Conexión exitosa a la base de datos')
        except mysql.connector.Error as err:
            print(f'Error: {err}')

    def closeconn(self):
        if self.conn.is_connected():
            self.conn.close()
            print('Conexión cerrada')