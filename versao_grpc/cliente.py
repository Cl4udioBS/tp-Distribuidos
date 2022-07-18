#talvez utilziar time
import time 
import grpc
import comunicacao_pb2
import comunicacao_pb2_grpc

def getRequisicaoCliente():
    while True:
        nome = input("Digite: (ENTER para sair) ")

        if nome == "":
            break

        msgRequest = comunicacao_pb2.MsgRequest (mensagem = "Hello", nome = nome)
        yield msgRequest
        time.sleep(1)

def run():
    with grpc.insecure_channel("localhost:50051") as canal:
        stub = comunicacao_pb2_grpc.ComunicarStub(canal)
        print("4. InteractingHello - Both Streaming")
        chamadaRpc = input("Which rpc would you like to make: ")

        if chamadaRpc == "4":
            respostas = stub.ComInterativa(getRequisicaoCliente())

            for resposta in respostas:
                print("Resposta a requisição recebida: ")
                print(resposta)

def main():
    try: 
       run()
    except:
        return print("Conexão indisponível...");

if __name__ == "__main__":
    main()