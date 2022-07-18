from concurrent import futures
#talvez utilziar time
import time 
import grpc
import comunicacao_pb2
import comunicacao_pb2_grpc

import rns
import cliente as c
from entidades import database as db
HOST = 'localhost';
PORT = '7777';


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


