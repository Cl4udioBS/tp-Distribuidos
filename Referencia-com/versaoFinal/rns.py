from entidades import database
import sqlite3




###RF01

def boasVindas(cliente):
    cliente.send('\t\t BEM VINDO AO kERO - SEU SD DE TROCAS DE CERVEJA'.encode('utf-8'));
    cliente.send('\n(SERVIDOR) Insira seu nome: '.encode('utf-8'));
    nome = cliente.recv(2048).decode('utf-8');     
    valido = autenticacao(nome.lower());
    if valido == 'T':
        try:
            cliente.send(f'(SERVIDOR) {nome}, vamos as trocas?!'.encode('utf-8'))
            listagemDeitens(cliente, nome)
            
            #RESTO DA LOGICA

        except:
            print('Usuario fora do Sistema!')
    else:
        cliente.send(f'(SERVIDOR) {nome}=> Não cadastrado !!!!\nDeseja realizar cadastro?'+
                                            '\n(S)im\t(N)ao'.encode('utf-8'))      
        resposta = (cliente.recv(2048).decode('utf-8')).lower();
        if (resposta == 's'):
            cadastroUsuario(nome,cliente)
        else:            
            cliente.send(f'(SERVIDOR) {nome} Sem cadastro, sem cerveja!'.encode('utf-8'))
            cliente.close()            


def autenticacao(nome):
    dadosLogin = [ ]
    try:
        dadosLogin = database.SelectTodosUsuarios('TPSD.db')
        cadastro = "F"
        for check in dadosLogin:
            if (check == nome):
                cadastro = 'T'
        return cadastro
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

def cadastroUsuario(nome, cliente):
    database.InsertUsuario('TPSD.db',nome, '1234')
    print(f'Usuario {nome} inserido com sucesso!')
    cliente.send(f'(SERVIDOR) Usuario < {nome} > inserido com sucesso!'.encode('utf-8'))
    

def listagemDeitens(cliente, nome):
    dadosListagem = [ ]
    try:
        cliente.send(f'(SERVIDOR) < {nome} > Confira as cervejas disponiveis \n\tem nosso BAR'.encode('utf-8'))
        cliente.send(f'(SERVIDOR)[PROPRIETARIO, CERVEJA, ABV, IBU, ESTILO]'.encode('utf-8'))
        dadosListagem = database.SelectTodasCervejas()
        if (len(dadosListagem) > 0):
            for breja in dadosListagem:
                if (breja[0]!=nome):
                    cliente.send(f'\n||PROPRIETARIO: {breja[0]} ||CERVEJA: {breja[1]} ||ABV: {breja[2]} ||IBU: {breja[3]} ||ESTILO:{breja[4]} ||'.encode('utf-8'))
            cliente.send(f'\n(SERVIDOR) < {nome} > E ai?! Vai querer?'.encode('utf-8'))
        else:
           cliente.send(f'\n(SERVIDOR) < {nome} >Desculpe, tente outro dia'.encode('utf-8'))
    except:
        print("Error: Sorry :/")
