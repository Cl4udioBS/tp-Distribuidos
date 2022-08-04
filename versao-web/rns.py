import database
import sqlite3


def autenticacao(usuario):
    dadosLogin = [ ]
    
    try:
        dadosLogin = database.SelectTodosUsuarios('TPSD.db')
        cadastro = "F"
        for check in dadosLogin:
            if (check == usuario):
                cadastro = "T"
        return cadastro
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

def cadastroUsuario(nome):
    response = database.InsertUsuario('TPSD.db',nome, '1234')
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


def cadastrarCerveja(cerveja, abv, ibu, estilo, nome   ):
  
    try:
        nomeCerveja = cerveja
        abv         = abv
        ibu         = ibu
        estilo      = estilo
        nome        = nome

        database.InsertCervejaBar("TPSD.db",nome,nomeCerveja,abv,ibu,estilo)
        return 200

    except:
        print("Erro no cadastro!")
        return 400
   
def solicitaTroca(indiceCervejaSolicit,indiceCervejaExec ):
   
    try:
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
        return response

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
            print(troca)
            database.TrocaTitularidade("TPSD.db",troca[0][3],troca[0][2])
            database.TrocaTitularidade("TPSD.db",troca[0][4],troca[0][1])
            
            return 200
        except:
            return 400
    else:
        try:
            database.RejeitaTroca("TPSD.db",indiceTroca)
            return 200
        except:
            return 400        

