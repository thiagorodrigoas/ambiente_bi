import pyodbc

CONFIG_DB = {
    'driver': 'ODBC Driver 17 for SQL Server',
    'server': 'localhost',
    'database': 'db_sistema',
    'username': 'sa',
    'password': 'admin',
    'timeout': '1',
    'autocommit': 'False'
}

#Conexão Banco de dados
def conecta_banco(kwargs):
    string_connection = 'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};timeout={timeout};autocommit={autocommit}'.format( driver = kwargs['driver'],
                                                                                                                                               server = kwargs['server'],
                                                                                                                                               database = kwargs['database'],
                                                                                                                                               username = kwargs['username'],
                                                                                                                                               password = kwargs['password'],
                                                                                                                                               timeout = kwargs['timeout'],
                                                                                                                                               autocommit = kwargs['autocommit']
                                                                                                                                               )
    cnxn = pyodbc.connect(string_connection)
    return cnxn

# Configura cursor a partir da conexão
def inicia_cursor(cnxn):
    cursor = cnxn.cursor()
    cursor.fast_executemany = True
    return cursor