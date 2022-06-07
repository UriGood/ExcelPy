from multiprocessing import connection
import mysql.connector
def conexionDb():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root', 
            password='',
            db='excelpy'
        )
        return connection
        # if connection.is_connected():
        #     print('conexión exitosa')
        #     info_server = connection.get_server_info()
        #     print(info_server)
        #     cursor = connection.cursor()
        #     cursor.execute("INSERT INTO registros (panel_number) VALUES('prueba654654')")
        #     connection.commit()
        #     print("registro insertado con exito")
    except Exception as ex:
        return ex