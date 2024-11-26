"""import pyodbc

# Configura los parámetros de conexión
server = 'localhost'  # Reemplaza con el nombre de tu servidor
database = 'SistemaHotel'  # Reemplaza con el nombre de tu base de datos
username = 'sa'  # Reemplaza con tu nombre de usuario
password = 'admin'  # Reemplaza con tu contraseña

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

"""
import sqlite3

# Archivo de la base de datos SQLite
db_name = "sistemahotel.db"

# Establece la conexión
conexion = sqlite3.connect(db_name)

# Asegurarse de habilitar claves foráneas
conexion.execute("PRAGMA foreign_keys = ON;")

def resultadoSQL(sql, params=None):
    """
    Ejecuta una consulta SELECT y devuelve los resultados.
    """
    cursor = conexion.cursor()
    try:
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
        filas = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error: {e}")
        filas = []
    finally:
        cursor.close()
    return filas

def ejecutarSQL(sql, params=None):
    """
    Ejecuta una consulta SQL (INSERT, UPDATE, DELETE) y confirma los cambios.
    """
    cursor = conexion.cursor()
    try:
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
        conexion.commit()
    except sqlite3.Error as e:
        raise Exception(f"Error al ejecutar la consulta SQL: {e}")
    finally:
        cursor.close()

def ejecutaSQL(sql, params=None):
    """
    Similar a ejecutarSQL, pero sin retorno de resultados.
    """
    cursor = conexion.cursor()
    try:
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
        conexion.commit()
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una tabla como ejemplo
    crear_tabla_sql = '''
    CREATE TABLE IF NOT EXISTS Cliente (
        DNI_Cliente INTEGER PRIMARY KEY,
        Nombre TEXT NOT NULL,
        Apellido TEXT NOT NULL
    );
    '''
    ejecutarSQL(crear_tabla_sql)

    # Insertar datos
    insertar_datos_sql = '''
    INSERT INTO Cliente (DNI_Cliente, Nombre, Apellido)
    VALUES (?, ?, ?)
    '''
    ejecutarSQL(insertar_datos_sql, (12345678, "Juan", "Pérez"))

    # Consultar datos
    consulta_sql = "SELECT * FROM Cliente"
    resultados = resultadoSQL(consulta_sql)
    for fila in resultados:
        print(fila)



