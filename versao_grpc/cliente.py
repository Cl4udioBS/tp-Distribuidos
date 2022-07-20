#talvez utilziar time
import time
import grpc
import comunicacao_pb2
import comunicacao_pb2_grpc


def run():
    LOGADO = 0
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = comunicacao_pb2_grpc.ComunicarStub(channel)

        while(True):
            if(LOGADO != 0):
                print("1:Geladeira ")
                print("2:Cadastrar cerveja")
                print("3:Ver sua Geladeira(Itens)")
                print("4:Aceitar/Recusar trocas")
                print("5:Kero Sair")
                rpc_call = input(" ESCOLHA UMA DAS OPCOES:")
                if rpc_call == "1":
                    listagemDeitensTroca(stub)                
                elif rpc_call == "5":
                    print("Fechando")
                    break
            else:
                conexaoLogin = login(stub)
                if (conexaoLogin != 1):
                    conexaoCadastro = cadastroUsuario(stub)                
                    if (conexaoCadastro == 0):
                        break
                LOGADO = 1

#=======================================================================================
            
def login(stub):
    print("\t EFETUAR LOGIN ==>")
    print("Digite seu nome para fazer login")
    print("")
    print("ENTER p/ sair")        
    n = input()
    LoginRequest = comunicacao_pb2.LoginRequest(usuario = n)
    usuarioNoSistema  = (stub.Login(LoginRequest)).message
    if ((usuarioNoSistema != 'T') or (n == "")):
        print("considere fazer cadastro")
        return 0        
    print("Bem vindo(a): ", LoginRequest.usuario)
    return 1

def cadastroUsuario(stub):
    print("\t EFETUAR CADASTRO ==>")
    print("Digite seu nome para fazer CADASTRO")
    print("")
    print("ENTER p/ sair")      
    n = input()
    LoginRequest = comunicacao_pb2.LoginRequest(usuario = n)
    if (n == ""):
        return 0
    stub.CadastroUsuario(LoginRequest)
    print("Bem vindo(a): ", LoginRequest.usuario)
    return 1

def listagemDeitensTroca (stub):
    print("\t NOSSA GELADEIRA ==>")
    geladeira = (stub.ListagemDeitensTroca(comunicacao_pb2.Vazia())).message

    print(geladeira)

    
           

if __name__ == "__main__":
    run()