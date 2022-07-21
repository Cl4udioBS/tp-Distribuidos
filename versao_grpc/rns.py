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

def responderSolicitacao(resSolicitacao,indiceTroca):
    if(resSolicitacao == 'k'):
        try:
            database.AceitaTroca("TPSD.db",indiceTroca)
            troca = database.SelectTrocaById(indiceTroca)
            database.TrocaTitularidade("TPSD.db",troca[0][3],troca[0][2])
            return 200
        except:
            return 400
    else:
        try:
            database.RejeitaTroca("TPSD.db",indiceTroca)
            return 200
        except:
            return 400        

