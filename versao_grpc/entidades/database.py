import sqlite3


nomeBanco = "TPSD.db"

##Criação, colocar script para fazer esses só no primeiro

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
                                nome_usuario text,
                                nome_cerveja text,
                                abv  text,
                                ibu text,
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
        sqlite_create_table_query = '''CREATE TABLE TROCACERVEJA (
                                id integer PRIMARY KEY AUTOINCREMENT,
                                id_cerveja_solicit integer ,
                                id_cerveja_exec integer,
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
        cursor.execute("INSERT INTO Usuarios values (?, ?)",(nome, senha))
        sqliteConnection.commit()
        print("DB: usuario inserido com sucesso", cursor.rowcount)
        
        cursor.close()
        return 200

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

def InsertCervejaBar(nomeBanco,nome_usuario, nome_cerveja,abv,ibu,estilo):
    print("dados chegando: ",nomeBanco,nome_usuario, nome_cerveja,abv,ibu,estilo)
    try:
        print("veio banco")
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
        print("cervevja inserida com sucesso", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

def InsertTrocaCervejas(nomeBanco,id_cerveja_solic, id_cerv_exec, solicitante, executor):
    try:
        sqliteConnection = sqlite3.connect(nomeBanco)
        cursor = sqliteConnection.cursor()
        sqlite_insert_query = """INSERT INTO TrocaCerveja
                          (
                            id_cerveja_solicit,
                            id_cerveja_exec,
                            nome_usr_solicitante,
                            nome_usr_executor,
                            status
                            )  VALUES  (?,?,?,?,?)"""
        data = (id_cerveja_solic, id_cerv_exec,solicitante,executor,"p")
        cursor.execute(sqlite_insert_query,data)
        sqliteConnection.commit()
        print("Troca inserida com sucesso\n", cursor.rowcount)
        cursor.close()
        return 200
    
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
        return 400

def SelectTodosUsuarios(nomeBanco):
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

def SelectTrocas(status):
    print("select trocas")
    try:
        sqliteConnection = sqlite3.connect(nomeBanco)
        cursor = sqliteConnection.cursor()
        sqlite_select_query = """SELECT * FROM TrocaCerveja where status = ?"""
        data = (status,)
        cursor.execute(sqlite_select_query,data)
        sqliteConnection.commit()
        records = cursor.fetchall()

        listaUsuarios = []
        for row in records:
            troca = [row[0],row[1], row[2], row[3], row[4], row[5]]
            print("row 4: ", row[4])
            listaUsuarios.append(troca)
    
        cursor.close()
        return listaUsuarios

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

def SelectTrocaById(id):
    print("select trocas")
    try:
        sqliteConnection = sqlite3.connect(nomeBanco)
        cursor = sqliteConnection.cursor()
        sqlite_select_query = """SELECT * FROM TrocaCerveja where id = ?"""
        data = (id,)
        cursor.execute(sqlite_select_query,data)
        sqliteConnection.commit()
        records = cursor.fetchall()

        listaUsuarios = []
        for row in records:
            troca = [row[0],row[1], row[2], row[3], row[4], row[5]]
            print("row 4: ", row[4])
            listaUsuarios.append(troca)
    
        cursor.close()
        return listaUsuarios

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

def SelectTrocasByUsrExec(nome):
    print("select trocas exec",nome)
    try:
        sqliteConnection = sqlite3.connect(nomeBanco)
        cursor = sqliteConnection.cursor()
        sqlite_select_query = """SELECT * FROM TrocaCerveja where nome_usr_executor = ? and status = p"""
        data = (nome,)
        cursor.execute(sqlite_select_query,data)
        sqliteConnection.commit()
        records = cursor.fetchall()

        listaUsuarios = []
        print("records: ", records)
        for row in records:
            troca = [row[0],row[1], row[2], row[3], row[4], row[5]]
            listaUsuarios.append(troca)
    
        cursor.close()
        return listaUsuarios

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

def SelectUsuarioByNome(nome):
    try:
        print("oi teste: ", nome)
        sqliteConnection = sqlite3.connect(nomeBanco)
        cursor = sqliteConnection.cursor()
        sqlite_select_query = """SELECT * FROM Usuarios where nome = ?"""
       
        cursor.execute(sqlite_select_query,(nome,))
        sqliteConnection.commit()
        records = cursor.fetchall()

        usuario = []
        for row in records:
            item = [row[0], row[1]]
            usuario.append(item)
    
        cursor.close()
        print("oi usuario: ", usuario)
        return usuario

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
            item = [row[0],row[1], row[2], row[3], row[4], row[5]]
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
            item = [row[0],row[1], row[2], row[3], row[4], row[5]]
            listacervejas.append(item)
    
        cursor.close()
        return listacervejas

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

def SelectCervejaByIdBar(id):
    try:
        sqliteConnection = sqlite3.connect(nomeBanco)
        cursor = sqliteConnection.cursor()
        sqlite_select_query = """SELECT * FROM BAR where id = ?"""
       
        cursor.execute(sqlite_select_query,(id,))
        sqliteConnection.commit()
        records = cursor.fetchall()

        listacervejas = []
        for row in records:
            item = [row[0],row[1], row[2], row[3], row[4], row[5]]
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
            item = [row[0],row[1], row[2], row[3], row[4], row[5]]
            listacervejas.append(item)
    
        cursor.close()
        return listacervejas

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

def AceitaTroca(nomeBanco,id_troca):
    try:
        sqliteConnection = sqlite3.connect(nomeBanco)
        cursor = sqliteConnection.cursor()
        sqlite_insert_query = """Update TrocaCerveja set status = ? where id = ?"""
        data = ("a",id_troca)
        cursor.execute(sqlite_insert_query,data)
      
        
        sqliteConnection.commit()
        print("Troca atualizada com sucesso", cursor.rowcount)

        cursor.close()
        #SelectUsersTroca(nomeBanco,id_troca)
    
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)



def RejeitaTroca(nomeBanco,id_troca):
    try:
        sqliteConnection = sqlite3.connect(nomeBanco)
        cursor = sqliteConnection.cursor()
        sqlite_insert_query = """Update TrocaCerveja set status = ? where id = ?"""
        data = ("r",id_troca)
        cursor.execute(sqlite_insert_query,data)
        sqliteConnection.commit()
        print("Troca atualizada com sucesso", cursor.rowcount)
        cursor.close()
    
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

def TrocaTitularidade(nomeBanco, nomeNovoDono,idCervejaExec):
    try:
        sqliteConnection = sqlite3.connect(nomeBanco)
        cursor = sqliteConnection.cursor()
        sqlite_insert_query = """Update Bar set nome_usuario = ? where id = ?"""
        data = (nomeNovoDono,idCervejaExec)
        print("data: ",data)
        cursor.execute(sqlite_insert_query,data)
        sqliteConnection.commit()
        print("Troca atualizada com sucesso", cursor.rowcount)
        cursor.close()
    
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)




def InicializaBD():
    try:

        try:
            sqlite3.connect('file:TPSD.db?mode=rw', uri=True)
        
        except:
            createDB("TPSD")
            CreateTableBar(nomeBanco)
            CreateTableUsuario(nomeBanco)
            CreateTableTrocas(nomeBanco)
            InsertUsuario(nomeBanco,"claudio","0")
            InsertUsuario(nomeBanco,"aryel","1")
            InsertCervejaBar(nomeBanco,"claudio","guinnes", 4.5,27,"irish stout")
            InsertCervejaBar(nomeBanco,"claudio","brahma", 4.8,18,"international lager")
            InsertCervejaBar(nomeBanco,"aryel","brahma", 4.8,18,"international lager")
            SelectTodasCervejas()
            InsertTrocaCervejas(nomeBanco, 3, 1, "aryel", "claudio")           
            trocasPendentes = SelectTrocas("p")
            print("trocas pendentes", trocasPendentes)

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)


def TesteBD():
    teste = SelectTodosUsuarios(nomeBanco)
    print("usuarios: ", teste)
    cervejas = SelectTodasCervejas()
    print("todas cervejas: ", cervejas)
    especifica = SelectCervejaByNome("brahma")
    print(especifica)
    test = SelectCervejaByUsuario("claudio")
    print("um usuario: ", test)

if __name__ == "__main__":
    InicializaBD()
    TesteBD()  
    