from concurrent import futures
#talvez utilziar time
import time 
import grpc
import comunicacao_pb2
import comunicacao_pb2_grpc
import rns
import cliente as c
from entidades import database as db


class ServidorKero(comunicacao_pb2_grpc.ComunicarServicer):
    def Login(self, request, context):
        print("Request Login")
        login = comunicacao_pb2.LoginReply()
        autenticacao = rns.autenticacao(request.usuario)
        print("Resposta Login: ", autenticacao)
        login.message = f"{autenticacao}"
        return login 

    def CadastroUsuario(self, request, context):
        print("Request Cadastro")
        cadastro = comunicacao_pb2.LoginReply()
        fazerCadastro = rns.cadastroUsuario(request.usuario)
        print("Resposta Cadastro: ", cadastro)
        cadastro.message = f"{fazerCadastro}"
        return cadastro 

    def ListagemDeitensTroca(self, request, context):
        print("Request Lista de Itens BAR")
        listaBar = comunicacao_pb2.ListaCervejaBar()
        listagemDeitensT = rns.listagemDeitensTroca()
        if (listagemDeitensT != 400):
            for cervejaBar in listagemDeitensT:
                cervejaDisponivel = comunicacao_pb2.CervejaBar()
                cervejaDisponivel.id = cervejaBar[0]
                cervejaDisponivel.dono = cervejaBar[1]
                cervejaDisponivel.cerveja = cervejaBar[2]
                cervejaDisponivel.abv = cervejaBar[3]
                cervejaDisponivel.ibu = cervejaBar[4]
                cervejaDisponivel.estilo = cervejaBar[5]
                listaBar.cerveja.append(cervejaDisponivel)          
        return listaBar
        

    def ListagemDeitensGeladeira(self, request, context):
        print("Request Lista de Itens GELADEIRA")
        listaGeladeira = comunicacao_pb2.ListaCervejaBar()
        listagemDeitensT = rns.listagemMeusItens(request.usuario)
        print(listagemDeitensT)
        if (listagemDeitensT != 400):
            for cervejaGeladeira in listagemDeitensT:
                cervejaDisponivel = comunicacao_pb2.CervejaBar()
                cervejaDisponivel.id = cervejaGeladeira[0]
                cervejaDisponivel.dono = cervejaGeladeira[1]
                cervejaDisponivel.cerveja = cervejaGeladeira[2]
                cervejaDisponivel.abv = cervejaGeladeira[3]
                cervejaDisponivel.ibu = cervejaGeladeira[4]
                cervejaDisponivel.estilo = cervejaGeladeira[5]
                listaGeladeira.cerveja.append(cervejaDisponivel)          
        else:
            listaGeladeira = '400'
        return listaGeladeira


    def CadastroCerveja(self, request, context):
        print("Request Cadastro Cerveja")
        cadastro = comunicacao_pb2.CadastroReply()
        fazerCadastroCerveja = rns.cadastrarCerveja(request)
        print("Resposta Cadastro: ", fazerCadastroCerveja)
        cadastro.message = 'STATUS: '+ str(fazerCadastroCerveja)
        return cadastro

    def TrocarCerveja(self, request, context):
        print("Request Troca de Cerveja")
        troca = comunicacao_pb2.TrocaReply()
        fazerTrocaCerveja = rns.solicitaTroca(request)
        print("Resposta Troca: ", fazerTrocaCerveja)
        troca.message = 'STATUS: '+ str(fazerTrocaCerveja)
        return troca


#=======================================================================================
    
def servidor():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    comunicacao_pb2_grpc.add_ComunicarServicer_to_server(ServidorKero(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()

def main():
    try: 
        print("SERVIDOR::Ativo!\n");
        db.InicializaBD()
        servidor()            
    except:
        return print("SERVIDOR :: ENCERRANDO SERVIDOR!\n");


if __name__ == "__main__":
    main()
