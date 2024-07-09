from db_conection import DBconn as db

def main():
    host = 'localhost';
    user = 'root';
    password = '';
    database = 'killcoronavirus'

    conn = db(host, user, password, database)
    conn.connect()