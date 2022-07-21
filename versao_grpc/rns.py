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
        dadosListagem = database.SelectTodasCervejas()
        if (len(dadosListagem) > 0):
            return dadosListagem
        else:
            return 404
    except:
        print("Error: Sorry :/")

def listagemMeusItens(nome):
    dadosListagem = [ ]
    try:
        dadosListagem = database.SelectCervejaByUsuario(nome)
        if (len(dadosListagem) > 0):
            return dadosListagem
        else:
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

def listarTrocasPendentes(usuario):
    trocas = database.SelectTrocas("p")
    if(len(trocas)>0):
        disponiveis = [] 
        for troca in trocas:
            if troca[4] == usuario:
                disponiveis.append(troca)                            
        try:
            return disponiveis                   
        except:
            return 400

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
