import pyodbc

Servidor = "SOLI-PC\MSSQLSERVER02"
Usuario = "soli"
Password = "admin"
Base_Datos = "AutopartesOcampo"

conn_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={Servidor};DATABASE={Base_Datos};UID={Usuario};PWD={Password}'

try:
    conexion = pyodbc.connect(conn_string)
    print("Conexión exitosa")
except pyodbc.Error as e:
    print("Ocurrió un error al conectar a SQL Server: ", e)
