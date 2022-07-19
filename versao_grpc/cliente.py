#talvez utilziar time
import time
import grpc
import comunicacao_pb2
import comunicacao_pb2_grpc

LOGADO = 0


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = comunicacao_pb2_grpc.ComunicarStub(channel)

        while(True):

            if(LOGADO != 0):
                print("1:Solicitar troca ")
                print("2:Cadastrar cerveja")
                print("3:Ver sua Geladeira(Itens)")
                print("4:Aceitar/Recusar trocas")
                print("5:Kero Sair")
                rpc_call = input(" ESCOLHA UMA DAS OPCOES:")
                if rpc_call == "1":
                    print("oi")                
                elif rpc_call == "5":
                    print("Fechando")
                    break

            else:
                conexaoLogin = login(stub)
                conexaoCadastro = cadastroUsuario(stub)
                if ((conexaoLogin | conexaoCadastro) == 0):
                    break
                break

            
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
    usuarioNoSistema  = (stub.CadastroUsuario(LoginRequest)).message
    print("LOOP: ", usuarioNoSistema)

    print("Bem vindo(a): ", LoginRequest.usuario)
    return 1        
           

if __name__ == "__main__":
    run()