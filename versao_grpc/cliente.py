#talvez utilziar time
import time
import grpc
import comunicacao_pb2
import comunicacao_pb2_grpc
import com2_pb2
import com2_pb2_grpc


def get_client_stream_requests():
    while True:
        name = input("Please enter a name (or nothing to stop chatting): ")

        if name == "":
            break

        hello_request = com2_pb2.HelloRequest(greeting = "Hello", name = name)
        yield hello_request
        time.sleep(1)

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = com2_pb2_grpc.GreeterStub(channel)
        logado = 0
        while(True):

            if(logado != 0):
                print("1:Solicitar troca ")
                print("2:Cadastrar cerveja")
                print("3:Ver sua Geladeira(Itens)")
                print("4:Aceitar/Recusar trocas")
                print("5:Kero Sair")
                rpc_call = input(" ESCOLHA UMA DAS OPCOES:")
                if rpc_call == "1":
                    print("oi")
                elif rpc_call == "2":
                    hello_request = com2_pb2.HelloRequest(greeting = "Bonjour", name = "YouTube")
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
                print("Digite seu nome para fazer login")
                n = input()
                LoginRequest = com2_pb2.Usuario(nome = n)
                hello_reply  = stub.Login(LoginRequest)
                print("Bem vindo(a): ", LoginRequest.nome)
                logado = 1
            
            

            

if __name__ == "__main__":
    run()