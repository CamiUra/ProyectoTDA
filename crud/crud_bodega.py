from db_conection import connect

def c_bod(prod_id, prod_nombre, prod_cantidad):
        try:
            conn = connect()
            cursor = conn.cursor()
            query = 'INSERT INTO bodega (prod_nombre, prod_cantidad) VALUES (%s,%s)'
            valores = (prod_nombre, prod_cantidad)
            cursor.execute(query, valores)
            conn.commit()
            print('Producto agregado a la bodega.')
            cursor.close()
            conn.close()
        except:
            print('Error al agregar el producto a la bodega.')

def r_bod():
    try:
        conn = connect()
        cursor = conn.cursor()
        query = 'SELECT * FROM bodega'
        cursor.execute(query)
        data = cursor.fetchall()
        print('--- Bodega ---')
        for rows in data:
            print(f'''ID: {rows[0]},
                Nombre Producto: {rows[1]},
                Cantidad: {rows[2]}''')
            cursor.close()
            conn.close()
    except:
        print('Error al mostrar la bodega.')

def u_bod(prod_id, prod_cantidad):
    try:
        conn = connect()
        cursor = conn.cursor()
        query = 'UPDATE bodega SET prod_cantidad = %s WHERE prod_id = %s'
        valores = (prod_cantidad, prod_id)
        cursor.execute(query, valores)
        conn.commit()
        print('Producto actualizado en la bodega.')
        cursor.close()
        conn.close()
    except:
        print('Error al actualizar el producto en la bodega.')

def d_bod(prod_id):
    try:
        conn = connect()
        cursor = conn.cursor()
        query = 'DELETE FROM bodega WHERE prod_id = %s'
        valores = (prod_id)
        cursor.execute(query, valores)
        conn.commit()
        print('Producto eliminado de la bodega.')
        cursor.close()
        conn.close()
    except:
        print('Error al eliminar el producto de la bodega.')