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
            #listagemDeitens(cliente, nome)
            SolicitaTroca(cliente,nome)
            
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
    

def listagemDeitensTroca(cliente, nome):
    dadosListagem = [ ]
    try:
        cliente.send(f'(SERVIDOR) < {nome} > Confira as cervejas disponiveis \n\tem nosso BAR'.encode('utf-8'))
        cliente.send(f'(SERVIDOR)[INDICE,PROPRIETARIO, CERVEJA, ABV, IBU, ESTILO]'.encode('utf-8'))
        dadosListagem = database.SelectTodasCervejas()
        if (len(dadosListagem) > 0):
            for breja in dadosListagem:
               
                if (breja[1]!=nome):
                    cliente.send(f'\n||Indice: {breja[0]} ||PROPRIETARIO: {breja[1]} ||CERVEJA: {breja[2]} ||ABV: {breja[3]} ||IBU: {breja[4]} ||ESTILO:{breja[5]} ||'.encode('utf-8'))
            cliente.send(f'\n(SERVIDOR) < {nome} > E ai?! Vai querer?'.encode('utf-8'))
            cliente.send(f'\n(SERVIDOR)[Bora] [Voltar]'.encode('utf-8'))
            
            resposta = cliente.recv(2048).decode('utf-8');
            
            if(resposta.lower() == "bora"):
                return 1
                #cliente.send(resposta.encode('utf-8'))
            else:
                return 0
        else:
           cliente.send(f'\n(SERVIDOR) < {nome} >Desculpe, tente outro dia'.encode('utf-8'))
    except:
        print("Error: Sorry :/")

def listagemMeusItens(cliente, nome):
    dadosListagem = [ ]
    try:
        cliente.send(f'(SERVIDOR) < {nome} > Essas são as cervejas que você cadastrou \n\tem nosso BAR'.encode('utf-8'))
        cliente.send(f'(SERVIDOR)[INDICE,PROPRIETARIO, CERVEJA, ABV, IBU, ESTILO]'.encode('utf-8'))
        dadosListagem = database.SelectTodasCervejas()
        if (len(dadosListagem) > 0):
            for breja in dadosListagem:
                if (breja[1]==nome):
                    cliente.send(f'\n||Indice: {breja[0]} ||PROPRIETARIO: {breja[1]} ||CERVEJA: {breja[2]} ||ABV: {breja[3]} ||IBU: {breja[4]} ||ESTILO:{breja[5]} ||'.encode('utf-8'))
        else:
           cliente.send(f'\n(SERVIDOR) < {nome} >Desculpe, tente outro dia'.encode('utf-8'))
           return 0
        return 1
    except:
        print("Error: Sorry :/")

def SolicitaTroca(cliente, nome):
    
    try:
        res = listagemDeitensTroca(cliente, nome)
        print("res: ",res)
        if(res == 1):
            cliente.send(f'\n(SERVIDOR) < {nome} > Incrivel, vou te mostrar as cervejas que você tem para oferecer numa troca!'.encode('utf-8'))
            listagemMeusItens(cliente,nome)
            cliente.send(f'\n(SERVIDOR) < {nome} > Agora você tem todas as informações para efetuar uma troca, vamos lá?!'.encode('utf-8'))
            cliente.send(f'\n(SERVIDOR) < {nome} > Escolha primeiro a cerveja que você deseja solicitar!'.encode('utf-8'))
            cliente.send(f'\n(SERVIDOR) < {nome} > É só digitar o indice da desejada'.encode('utf-8'))


    except:
        print("Error: Sorry :/")