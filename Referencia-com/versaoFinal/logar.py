from entidades import DB
import sqlite3

class Usuario():

    def __init__(self, nome, senha):
        self.__nome = nome
        self.__senha = senha


def boasVindas(cliente):
    cliente.send('\t\t BEM VINDO AO kERO - SEU SD DE TROCAS DE CERVEJA\n'.encode('utf-8'));
    cliente.send('Insira seu nome: '.encode('utf-8'));
    nome = cliente.recv(2048).decode('utf-8');
    print('Nome:', nome, type(nome))

    cliente.send('Insira sua senha:'.encode('utf-8'));
    senha = cliente.recv(2048).decode('utf-8');
    print('Senha:', senha, type(senha))
    
    #valido = Authentication(nome,senha);   
    #print ('valido' + valido); 



def Authentication(nome,senha):
    try:
        
        #sqliteConnection = sqlite3.connect('testePy')
        #cursor = sqliteConnection.cursor()
        #sqlite_select_query = """SELECT * from Usuarios WHERE nome=? and senha=?"""
        #cursor.execute(sqlite_select_query,(nome,senha));
        #sqliteConnection.commit()
        #records = cursor.fetchall()
        #print(records); 
        #cursor.close()

        teste = DB.SelectUsuarioByNome(nome)
        print("oi",teste)
           

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
