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
                elif rpc_call == "2":
                    hello_request = comunicacao_pb2.HelloRequest(greeting = "Bonjour", name = "YouTube")
                    hello_replies = stub.ParrotSaysHello(hello_request)

                    for hello_reply in hello_replies:
                        print("ParrotSaysHello Response Received:")
                        print(hello_reply)
                elif rpc_call == "3":
                    delayed_reply = stub.ChattyClientSaysHello(get_client_stream_requests())

                    print("ChattyClientSaysHello Response Received:")
                    print(delayed_reply)
                elif rpc_call == "4":
                    responses = stub.InteractingHello(get_client_stream_requests())

                    for response in responses:
                        print("InteractingHello Response Received: ")
                        print(response)
                elif rpc_call == "5":
                    print("Fechando")
                    break

            else:
                sair = login(stub)
                if (sair == 0):
                    break
                break

            
def login(stub):
    loop = "F"
    while (loop == "F"):
        print("\t EFETUAR LOGIN ==>")
        print("Digite seu nome para fazer login")
        print("")
        print("ENTER p/ sair")


        
        n = input()
        LoginRequest = comunicacao_pb2.LoginRequest(usuario = n)
        loop  = (stub.Login(LoginRequest)).message
        print("LOOP: ",loop)
        if (n == ""):
            return 0
    print("Bem vindo(a): ", LoginRequest.usuario)
    LOGADO = 1          
           

if __name__ == "__main__":
    run()