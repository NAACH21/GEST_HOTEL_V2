import pyodbc

# Configura los parámetros de conexión
server = 'localhost'  # Reemplaza con el nombre de tu servidor
database = 'SistemaHotel1'  # Reemplaza con el nombre de tu base de datos
username = 'sa'  # Reemplaza con tu nombre de usuario
password = '123456789'  # Reemplaza con tu contraseña

# Establece la conexión
conexion = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=' + server + ';'
    'DATABASE=' + database + ';'
    'UID=' + username + ';'
    'PWD=' + password
)

def resultadoSQL(sql):
    cursor = conexion.cursor()
    try:
        cursor.execute(sql)
        filas = cursor.fetchall()

    except pyodbc.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
    return filas

def ejecutarSQL(sql, params=None):
    cursor = conexion.cursor()
    try:
        cursor.execute(sql, params)
        conexion.commit()
    except pyodbc.Error as e:
        raise Exception(f"Error al ejecutar la consulta SQL: {e}")
    finally:
        cursor.close()
def resultadoSQL(sql):
    cursor = conexion.cursor()
    try:
        cursor.execute(sql)
        filas = cursor.fetchall()
        for fila in filas:
            #print(fila)
            pass

    except pyodbc.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
    return filas

def ejecutaSQL(sql):
    cursor = conexion.cursor()
    try:
        cursor.execute(sql)
        conexion.commit()
    except pyodbc.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()




