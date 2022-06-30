from entidades import DB
import sqlite3


#and senha=?



def boasVindas(cliente):
    cliente.send('\t\t BEM VINDO AO kERO - SEU SD DE TROCAS DE CERVEJA'.encode('utf-8'));
    cliente.send('\n(SERVIDOR) Insira seu nome: '.encode('utf-8'));
    nome = cliente.recv(2048).decode('utf-8');     
    valido = Authentication(nome.lower());
    #print(valido)  
    if valido == 'T':
        try:
            cliente.send(f'(SERVIDOR) {nome}, vamos as trocas?!'.encode('utf-8'))
        except:
            print('Usuario fora do Sistema!')
    else:
        print("Não cadastrado !!!!\nDeseja realizar cadastro?")


def Authentication(nome):
    dadosLogin = [ ]
    try:         
        sqliteConnection = sqlite3.connect('TPSD.db')
        cursor = sqliteConnection.cursor()
        cursor.execute("SELECT * from Usuarios");
        records = cursor.fetchall()
        for row in records:
            #print("nome: ",row[0]) #RETIRAR
            dadosLogin.append(row[0].strip())
        cursor.close()
        #redeUsuarios = dadosLogin
        cadastro = "F"

        for check in dadosLogin:
            if (check == nome):
                cadastro = 'T'
        return cadastro            
  

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
