#talvez utilziar time
from pickle import FALSE, TRUE
import time
import grpc
import comunicacao_pb2
import comunicacao_pb2_grpc


def run():
    LOGADO = 0
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = comunicacao_pb2_grpc.ComunicarStub(channel)

        print("\t EFETUAR LOGIN ==>")
        print("Digite seu nome para fazer login")
        print("")
        print("ENTER p/ sair") 
        usuario = str(input().lower())
        while(True):
       
            if(LOGADO != 0):                
                print("\tMENU")
                print("1:BAR - itens p/ troca ")
                print("2:Cadastrar cerveja")
                print("3:Ver sua Geladeira(Itens)")
                print("4:Enviar pedido de troca")
                print("5:Listar TROCAS PENDENTES")                                
                print("6:Aceitar/Recusar trocas")
                print("7:Kero Sair")
                rpc_call = input(" ESCOLHA UMA DAS OPCOES:")
                if rpc_call == "1":
                    listagemDeitensTroca(stub)  
                if rpc_call == "2":
                    cadastroCerveja(stub, usuario)
                if rpc_call == "3":
                    listagemGeladeira(stub, usuario)
                if rpc_call == "4":
                    if (listagemGeladeira(stub, usuario) == 400):
                        print("Necessario ter cervejas cadastradas")
                        return
                    solicitaTroca(stub, usuario)
                if rpc_call == "5":
                    listagemTrocasPendentes(stub, usuario)
                elif rpc_call == "6":
                    responderSolicitacao(stub, usuario)
                elif rpc_call == "7":
                    print("Fechando")
                    break
            else:
                conexaoLogin = login(stub, usuario)
                LOGADO = 1
                if (conexaoLogin != 1):
                    conexaoCadastro = cadastroUsuario(stub, usuario)            
                    if (conexaoCadastro == 0):
                        break
                    LOGADO = 1


#=======================================================================================
            
def login(stub, n):
    LoginRequest = comunicacao_pb2.LoginRequest(usuario = n)
    usuarioNoSistema  = (stub.Login(LoginRequest)).message
    if ((usuarioNoSistema != 'T') or (n == "")):
        print("considere fazer cadastro")
        return 0        
    print("Bem vindo(a): ", LoginRequest.usuario)
    return 1

def cadastroUsuario(stub, usuarioI):
    print("\t EFETUAR CADASTRO ==>")
    print(f"{usuarioI}: digite seu nome novamente para fazer CADASTRO")
    print("")
    print("ENTER p/ sair")      
    n = input()
    LoginRequest = comunicacao_pb2.LoginRequest(usuario = usuarioI)
    if (n == ""):
        return 0
    stub.CadastroUsuario(LoginRequest)
    print("Bem vindo(a): ", LoginRequest.usuario)
    return 1
    
def solicitaTroca(stub, usuarioI):
    print("\t SOLICITAR TROCA ==>")
    listagemDeitensTroca(stub)
    print(f"{usuarioI}: Escolha primeiro a cerveja que você deseja solicitar!\nÉ só digitar o indice da desejada")
    indiceCervejaExecI = input()
    print("Veja sua geladeira novamente:")
    listagemGeladeira(stub, usuarioI)
    print(f"{usuarioI}: Agora só escolher o indice da cerveja que você deseja dar em troca")
    indiceCervejaSolicitI = input()
    TrocaRequest = comunicacao_pb2.TrocaRequest(indiceCervejaExec = indiceCervejaExecI,indiceCervejaSolicit = indiceCervejaSolicitI )
    troca = stub.TrocarCerveja(TrocaRequest)
    if (troca.message == '200'):
        print('Pedido de troca enviado')
    else:
        print('Houve um erro no seu pedido\n')

def responderSolicitacao(stub, usuarioI):
    print("\t RESPONDER TROCA ==>")
    listagemTrocasPendentes(stub, usuarioI)
    print("Digite o indice da troca que deseja responder")
    indiceTroca = input()
    print("SHOW!Agora digite se deseja realizar a troca ou rejeitar a solicitação")
    print("[ (K)ero p/ aceitar  | Qualquer coisa para rejeitar ] ")
    resSolicitacao = input().lower()
    ResponderSolicitacaoRequest = comunicacao_pb2.ResponderSolicitacaoRequest(indiceTroca = indiceTroca,resSolicitacao = resSolicitacao)
    resposta = stub.ResponderSolicitacao(ResponderSolicitacaoRequest)
    if (resposta.message == '200'):
        print('Troca aceita/recusada com SUCESSO!')
    else:
        print('Houve um erro na sua resposta\n')

def listagemTrocasPendentes(stub, usuarioI):
    print("\t SUAS TROCAS ==>")
    trocas = stub.ListagemTrocasPendentes(comunicacao_pb2.ListaTrocaRequest(usuario = usuarioI))
    if (trocas):
        print(trocas)
        print("^ Todas as trocas listadas | Vazio (Cadastre uma troca)")

def listagemDeitensTroca(stub):
    print("\t NOSSO BAR ==>")
    bar = stub.ListagemDeitensTroca(comunicacao_pb2.Vazia())
    print(bar)

def listagemGeladeira(stub, usuarioI):
    print("\t SUA GELADEIRA ==>")
    geladeira = stub.ListagemDeitensGeladeira(comunicacao_pb2.ListaGeladeiraRequest(usuario = usuarioI))
    if (geladeira):
        print(geladeira)
        print("^ Todos os itens listados | Vazio (Cadastre alguma cerveja)")

def cadastroCerveja(stub, usuario):
    while (TRUE):
        print("\t CADASTRAR CERVEJA ==>")
        nome = usuario
        print(f'\n(SERVIDOR) < {usuario} > Vamos cadastrar uma cerveja')
        print('\ndigite o nome cerveja')
        cerveja = input()
        print("\nAgora digite o ABV (ABV é a sigla para ALCOHOL BY VOLUME, ou quão alcoolico é um exemplar")
        abv = input()
        print("\nAgora digite o IBU (IBU é a sigla para International Bitterness Units, ou o quão amargo é um exemplar")
        ibu = input()
        print(f'\nTa quaaaase! Digite agora o estilo')
        estilo = input()
        print('\nConfirma as informações pra gente?')
        print(f'\nnome: {cerveja} ABV: {abv} IBU: {ibu} estilo:{estilo}')
        confirmacao = input('\n[S]im [N]ao\n').lower()
        if confirmacao == "s":
            itemCadastro = comunicacao_pb2.CervejaCadastro(nome = nome, cerveja = cerveja, ibu = ibu, abv = abv, estilo = estilo)
            cadastro = stub.CadastroCerveja(itemCadastro)
            print('CLIENTE:',cadastro)
            outroCadastro = input('Realizar outro cadastro??\n [S]im [N]ao\n')
            if outroCadastro != "s":
                break

    
           

if __name__ == "__main__":
    run()