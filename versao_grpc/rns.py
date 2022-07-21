from entidades import database
import sqlite3


def autenticacao(usuario):
    dadosLogin = [ ]
    
    try:
        dadosLogin = database.SelectTodosUsuarios('TPSD.db')
        cadastro = "F"
        print(usuario)
        for check in dadosLogin:
            if (check == usuario):
                cadastro = "T"
        return cadastro
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

def cadastroUsuario(nome):
    response = database.InsertUsuario('TPSD.db',nome, '1234')
    print(f'SERVIDOR: Usuario {nome} inserido com sucesso!')
    return response

 
def listagemDeitensTroca():
    dadosListagem = [ ]
    try:
        ##cliente.send(f'(SERVIDOR) < {nome} > Confira as cervejas disponiveis \n\tem nosso BAR'.encode('utf-8'))
        ##cliente.send(f'(SERVIDOR)[INDICE,PROPRIETARIO, CERVEJA, ABV, IBU, ESTILO]'.encode('utf-8'))
        dadosListagem = database.SelectTodasCervejas()
        if (len(dadosListagem) > 0):
            return dadosListagem
            #!MOVER PARA CLIENTE OU INTERFACE GRÁFICA
            """
            for breja in dadosListagem:
               
                if (breja[1]!=nome):
                    cliente.send(f'\n||Indice: {breja[0]} ||PROPRIETARIO: {breja[1]} ||CERVEJA: {breja[2]} ||ABV: {breja[3]} ||IBU: {breja[4]} ||ESTILO:{breja[5]} ||'.encode('utf-8'))
            cliente.send(f'\n(SERVIDOR) < {nome} > E ai?! Vai querer?'.encode('utf-8'))
            cliente.send(f'\n(SERVIDOR)[Bora] [Voltar]'.encode('utf-8'))
            
            resposta = cliente.recv(2048).decode('utf-8');
            
            if(resposta.lower() == "bora"):
                return 1
            else:
                return 0
                """
        else:
            return 404
           #cliente.send(f'\n(SERVIDOR) < {nome} >Desculpe, tente outro dia'.encode('utf-8'))
    except:
        print("Error: Sorry :/")

def listagemMeusItens(nome):
    dadosListagem = [ ]
    try:
        #cliente.send(f'(SERVIDOR) < {nome} > Essas são as cervejas que você cadastrou \n\tem nosso BAR'.encode('utf-8'))
        #cliente.send(f'(SERVIDOR)[INDICE,PROPRIETARIO, CERVEJA, ABV, IBU, ESTILO]'.encode('utf-8'))
        dadosListagem = database.SelectCervejaByUsuario(nome)
        if (len(dadosListagem) > 0):
            return dadosListagem
            """
            for breja in dadosListagem:
                cliente.send(f'\n||Indice: {breja[0]} ||PROPRIETARIO: {breja[1]} ||CERVEJA: {breja[2]} ||ABV: {breja[3]} ||IBU: {breja[4]} ||ESTILO:{breja[5]} ||'.encode('utf-8'))
            return 1       
            """ 
        else:
            #cliente.send(f'\n(SERVIDOR) < {nome} >Você não tem itens cadastrados'.encode('utf-8'))
            return 400
    except:
        print("Error: Sorry :/")
        return 400


def cadastrarCerveja(dadosCerveja):
  
    try:
        nomeCerveja = dadosCerveja.cerveja
        abv         = dadosCerveja.abv
        ibu         = dadosCerveja.ibu
        estilo      = dadosCerveja.estilo
        nome        = dadosCerveja.nome

        database.InsertCervejaBar("TPSD.db",nome,nomeCerveja,abv,ibu,estilo)
        return 200

    except:
        print("Erro no cadastro!")
        return 400

     


def solicitaTroca(dadosTroca):
    indiceCervejaSolicit    = dadosTroca.indiceCervejaSolicit
    indiceCervejaExec       = dadosTroca.indiceCervejaExec
    
    try:
        #!Validar se tem itens no cliente
        dadosCervExec = database.SelectCervejaByIdBar(indiceCervejaExec)
        dadosCervSolic = database.SelectCervejaByIdBar(indiceCervejaSolicit)
        for breja in dadosCervSolic:
            solicitante = breja[1]
        for breja2 in dadosCervExec:
            executor = breja2[1]
        response = database.InsertTrocaCervejas("TPSD.db",indiceCervejaSolicit,indiceCervejaExec,solicitante,executor)
        return response

    except:
        print("Error: Sorry :/")
        response = 400



def ListarTrocasPendentes(cliente,nome):
    trocas = database.SelectTrocas("p")
    if(len(trocas)>0):
        #enviaMsgServ(f"\tEssas são as trocas pendentes do {nome}: ", cliente)  
        trocasRes = [] 
        trocasAux = []
        for troca in trocas:
            if troca[4] == nome:
                try:
                    #!mudar para cliente
                    '''                    
                    cervejaSolict = database.SelectCervejaByIdBar(troca[1])
                    cervejaExec = database.SelectCervejaByIdBar(troca[2])

                    enviaMsgServ(f"|| Indice: {troca[0]} ||",cliente)
                    enviaMsgServ(f"|| Cerveja oferecida: {cervejaSolict} ||",cliente)
                    enviaMsgServ(f"|| Cerveja solicitada: {cervejaExec} ||",cliente)
                    '''

                    return troca
                except:
                    return 400
                    #enviaMsgServ("ops!! tivemos um problema, tente novamente mais tarde!",cliente);

"""
        enviaMsgServ("Deseja Responder alguma solicitação?",cliente)
        enviaMsgServ("[Kero(1)] [Agora não(0)]",cliente)
        resposta = recebeMsgServ(cliente)
        if(resposta == '1'):
            enviaMsgServ(f"Agora digite o indice da troca que deseja responder",cliente)
            index = recebeMsgServ(cliente)
            enviaMsgServ(f"SHOW!Agora digite se deseja realizar a troca ou rejeitar a solicitação",cliente)
            enviaMsgServ(f"[Kero(1)] [Rejeitar Solicitação(0)]",cliente)
            rej = recebeMsgServ(cliente)
            if(rej == '1'):
                try:
                    database.AtualizaTrocaCervejas("TPSD.db",index,"a")
                    enviaMsgServ(f"Troca foi aceita",cliente)
                except:
                    enviaMsgServ("ops!! tivemos um problema, tente novamente mais tarde!");
            else:
                try:
                    database.AtualizaTrocaCervejas("TPSD.db",index,"r")
                    enviaMsgServ("Ok solicitação excluida")
                except:
                    enviaMsgServ("ops!! tivemos um problema, tente novamente mais tarde!");

        else:
              enviaMsgServ("Ok retornando!!")
"""

def responderSolicitacao(resSolicitacao,indiceTroca,solic,exec):
    if(resSolicitacao == '1'):
        try:
            database.AceitaTroca("TPSD.db",indiceTroca,solic,exec)
            troca = database.SelectTrocaById(indiceTroca)
            #!generalizar depois
            database.TrocaTitularidade("TPSD.db",solic,troca[0][2])
            #enviaMsgServ(f"Troca foi aceita",cliente)
            return 200
        except:
            return 400
            #enviaMsgServ("ops!! tivemos um problema, tente novamente mais tarde!");
    else:
        try:
            database.RejeitaTroca("TPSD.db",indiceTroca,solic,exec)
            return 200
        except:
            return 400

           
     
def ListarTrocasPendentesUsr(usuario):
    trocas = database.SelectTrocasByUsrExec(usuario)
    if(len(trocas)>0):
        return trocas
        """
        enviaMsgServ("\tEssas são as trocas pendentes que você tem: ", cliente)
        for troca in trocas:
            cervejaSolict = database.SelectCervejaByIdBar(troca[1])
            cervejaExec = database.SelectCervejaByIdBar(troca[2])
           
            cliente.send(f'\n|| oiIndice: {troca[0]} ||CERVEJA OFERECIDA: {cervejaSolict} ||CERVEJA SOLICITADA: {cervejaExec} '.encode('utf-8'))
        """
    return 400
