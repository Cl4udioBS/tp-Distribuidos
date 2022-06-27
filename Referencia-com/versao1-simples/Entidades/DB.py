import sqlite3

##Criação, colocar scrpt ra fazer esses só no primeiro

def createDB(nome):
    db = nome+'.db'
    try:
        sqliteConnection = sqlite3.connect(db)
        cursor = sqliteConnection.cursor()
        print("Banco criado com sucesso")

        sqlite_select_Query = "select sqlite_version();"
        cursor.execute(sqlite_select_Query)
        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

def CreateTableUsuario(nomeDb):
    try:
        sqliteConnection = sqlite3.connect(nomeDb)
        cursor = sqliteConnection.cursor()
        sqlite_create_table_query = '''CREATE TABLE Usuarios (
                                nome TEXT PRIMARY KEY,
                                senha text NOT NULL
                                );'''
        
        cursor = sqliteConnection.cursor()
       
        cursor.execute(sqlite_create_table_query)
        sqliteConnection.commit()
      
        cursor.close()


    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

def CreateTableBar(nomeDb):
    try:
        sqliteConnection = sqlite3.connect(nomeDb)
        cursor = sqliteConnection.cursor()
        sqlite_create_table_query = '''CREATE TABLE BAR (
                                id integer PRIMARY KEY AUTOINCREMENT,
                                nome_usuario text 0F,
                                nome_cerveja text,
                                abv  real,
                                ibu integer,
                                estilo text,
                                FOREIGN KEY(nome_usuario) REFERENCES Usuarios(nome)
                                );'''
        
        cursor = sqliteConnection.cursor()
       
        cursor.execute(sqlite_create_table_query)
        sqliteConnection.commit()
      
        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

def CreateTableTrocas(nomeDb):
    try:
        sqliteConnection = sqlite3.connect(nomeDb)
        cursor = sqliteConnection.cursor()
        sqlite_create_table_query = '''CREATE TABLE TROCAS (
                                id integer PRIMARY KEY AUTOINCREMENT,
                                id_cerveja_solicitante integer ,
                                id_cerveja_executor integer,
                                nome_usr_solicitante  text,
                                nome_usr_executor text,
                                status text
                                );'''
        
        cursor = sqliteConnection.cursor()
       
        cursor.execute(sqlite_create_table_query)
        sqliteConnection.commit()
      
        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

##Insert e Selects usados durante a execução do sistema
def InsertUsuario(nomeBanco,nome, senha):
    try:
        sqliteConnection = sqlite3.connect(nomeBanco)
        cursor = sqliteConnection.cursor()
        sqlite_insert_query = """INSERT INTO Usuarios
                          (nome, senha)  VALUES  (?,?)"""
        data = (nome, senha)
        cursor.execute(sqlite_insert_query,data)
        sqliteConnection.commit()
        print("usuario inserido com sucesso", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

def InsertCervejaBar(nomeBanco,nome_usuario, nome_cerveja,abv,ibu,estilo):
    try:
        sqliteConnection = sqlite3.connect(nomeBanco)
        cursor = sqliteConnection.cursor()
        sqlite_insert_query = """INSERT INTO BAR
                          (nome_usuario,
                          nome_cerveja,
                          abv,
                          ibu,
                          estilo)  VALUES  (?,?,?,?,?)"""
        data = (nome_usuario, nome_cerveja,abv,ibu,estilo)
        cursor.execute(sqlite_insert_query,data)
        sqliteConnection.commit()
        print("cerevja inserido com sucesso", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)


def SelectTodosUsuarios():
    try:
        sqliteConnection = sqlite3.connect(nomeBanco)
        cursor = sqliteConnection.cursor()
        sqlite_select_query = """SELECT * FROM Usuarios"""
        cursor.execute(sqlite_select_query)
        sqliteConnection.commit()
        records = cursor.fetchall()

        listaUsuarios = []
        for row in records:
            listaUsuarios.append(row[0])
    
        cursor.close()
        return listaUsuarios

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

def SelectTodasCervejas():
    try:
        sqliteConnection = sqlite3.connect(nomeBanco)
        cursor = sqliteConnection.cursor()
        sqlite_select_query = """SELECT * FROM BAR"""
        cursor.execute(sqlite_select_query)
        sqliteConnection.commit()
        records = cursor.fetchall()

        listacervejas = []
        for row in records:
            item = [row[1], row[2], row[3], row[4], row[5]]
            listacervejas.append(item)
    
        cursor.close()
        return listacervejas

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)



def SelectCervejaByNome(nome):
    try:
        sqliteConnection = sqlite3.connect(nomeBanco)
        cursor = sqliteConnection.cursor()
        sqlite_select_query = """SELECT * FROM BAR where nome_cerveja = ?"""
       
        cursor.execute(sqlite_select_query,(nome,))
        sqliteConnection.commit()
        records = cursor.fetchall()

        listacervejas = []
        for row in records:
            item = [row[1], row[2], row[3], row[4], row[5]]
            listacervejas.append(item)
    
        cursor.close()
        return listacervejas

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

def SelectCervejaByUsuario(nome_usuario):
    try:
        sqliteConnection = sqlite3.connect(nomeBanco)
        cursor = sqliteConnection.cursor()
        sqlite_select_query = """SELECT * FROM BAR where nome_usuario = ?"""
       
        cursor.execute(sqlite_select_query,(nome_usuario,))
        sqliteConnection.commit()
        records = cursor.fetchall()

        listacervejas = []
        for row in records:
            item = [row[1], row[2], row[3], row[4], row[5]]
            listacervejas.append(item)
    
        cursor.close()
        return listacervejas

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)



if __name__ == "__main__":
    nomeBanco = "testePy"
    ##createDB(nomeBanco)
    #CreateTableUsuario(nomeBanco)
    #InsertUsuario(nomeBanco,"claudio","generico")
    
    ##InsertUsuario(nomeBanco,"aryel","mmaisum")
    teste = SelectTodosUsuarios()
    print("usuarios: ", teste)
    #InsertCervejaBar(nomeBanco,"claudio","guinnes", 4.5,27,"irish stout")
    #InsertCervejaBar(nomeBanco,"claudio","brahma", 4.8,18,"international lager")
    cervejas = SelectTodasCervejas()
    print("todas cervejas: ", cervejas)
    especifica = SelectCervejaByNome("brahma")
    print(especifica)
    InsertCervejaBar(nomeBanco,"aryel","brahma", 4.8,18,"international lager")
    test = SelectCervejaByUsuario("claudio")
    print("um usuario: ", test)
    CreateTableTrocas(nomeBanco)
    ##CreateTableBar(nomeBanco)
