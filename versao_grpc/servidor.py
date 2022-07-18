from concurrent import futures
#talvez utilziar time
import time 
import grpc
import comunicacao_pb2
import comunicacao_pb2_grpc
import com2_pb2
import com2_pb2_grpc
import rns
import cliente as c
from entidades import database as db
HOST = 'localhost';
PORT = '7777';

class GreeterServicer(com2_pb2_grpc.GreeterServicer):
    def Login(self, request, context):
        print("Request Login")
        print(request)
        hello_reply = com2_pb2.HelloReply()
        autenticacao = rns.autenticacao(request)
        print("tipo resposta autenticação: ", autenticacao)
        #print("tipo msg message: ", type(msgOk.message))
        #print("response.message",response.message)
        hello_reply.message = f"{autenticacao}"
        return hello_reply
    
    def ParrotSaysHello(self, request, context):
        print("ParrotSaysHello Request Made:")
        print(request)

        for i in range(3):
            hello_reply = com2_pb2.HelloReply()
            hello_reply.message = f"{request.greeting} {request.name} {i + 1}"
            yield hello_reply
            time.sleep(3)

    def ChattyClientSaysHello(self, request_iterator, context):
        delayed_reply = com2_pb2.DelayedReply()
        for request in request_iterator:
            print("ChattyClientSaysHello Request Made:")
            print(request)
            delayed_reply.request.append(request)

        delayed_reply.message = f"You have sent {len(delayed_reply.request)} messages. Please expect a delayed response."
        return delayed_reply

    def InteractingHello(self, request_iterator, context):
        for request in request_iterator:
            print("InteractingHello Request Made:")
            print(request)

            hello_reply = com2_pb2.HelloReply()
            hello_reply.message = f"{request.greeting} {request.name}"

            yield hello_reply

def servidor():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    com2_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()

def main():
    try: 
        print("SERVIDOR::Ativo!\n");
        db.InicializaBD()
        servidor()            
    except:
        return print("SERVIDOR::Falha na inicialização!\n");


if __name__ == "__main__":
    main()

"""
class ServidorDeTrocas(comunicacao_pb2_grpc.ComunicarServicer):
    def ComInterativa(self, request_iterator, context):
        for requisicao in request_iterator:
            print("Requisição Feita")
            print(requisicao)

            msgReply = comunicacao_pb2.MsgReply()
            msgReply.mensagem = "Boas vindas"

            yield msgReply

def main():
    try: 
        print("SERVIDOR::Ativo!\n");
        db.InicializaBD()
        servidor()            
    except:
        return print("SERVIDOR::Falha na inicialização!\n");

def servidor():
    servidorOnline = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    comunicacao_pb2_grpc.add_ComunicarServicer_to_server(comunicacao_pb2_grpc.ComunicarServicer(), servidorOnline)
    servidorOnline.add_insecure_port('localhost:50051')
    servidorOnline.start()
    servidorOnline.wait_for_termination()

if __name__ == "__main__":
    main()

"""
