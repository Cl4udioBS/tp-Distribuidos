import sqlite3


def createDB(nome):
    db = nome+'.db'
    try:
        sqliteConnection = sqlite3.connect(db)
        cursor = sqliteConnection.cursor()
        print("Banco criado com sucesso")

        sqlite_select_Query = "select sqlite_version();"
        cursor.execute(sqlite_select_Query)
        record = cursor.fetchall()
        print("SQLite Database Version is: ", record)
        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    
    
##! geladeira(lista de cervejas que o usuario tem) é uma tabela, colocar relacionamento aqui
def CreateTableUsuario(nomeDb):
    try:
        sqliteConnection = sqlite3.connect(nomeDb)
        cursor = sqliteConnection.cursor()
        sqlite_create_table_query = '''CREATE TABLE Usuarios (
                                nome TEXT PRIMARY KEY,
                                senha text NOT NULL,
                                idGeladeira number NOT NULL 
                                );'''
        
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute(sqlite_create_table_query)
        sqliteConnection.commit()
        print("SQLite table created")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

##! create table geladeira?


##! como interpolar strings em python?
def InsertUsuario(nomeBanco,nome, senha):
    try:
        sqliteConnection = sqlite3.connect(nomeBanco)
        cursor = sqliteConnection.cursor()
        sqlite_insert_query = """INSERT INTO Usuarios
                          (nome, senha)  VALUES  ('aryel', 'Demo Text')"""
        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        print("usuario inserido com sucesso", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

    
if __name__ == "__main__":
    nomeBanco = "testePy"
    createDB(nomeBanco)
    #CreateTableUsuario(nomeBanco)
    InsertUsuario(nomeBanco,"aryel","teste")
    
