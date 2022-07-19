from entidades import database
import sqlite3



def enviaMsgServ(msg, cliente):
    try:
        cliente.send(f'\n(SERVIDOR): {msg}'.encode('utf-8'));
        print(f"\nMsg enviada para: {cliente}!\n")
    except:
        print('Falha no envio!\n');
        cliente.close();

def recebeMsgServ(cliente):
    try:
        msg = cliente.recv(2048).decode('utf-8'); #socket transmite em bytes
        return msg
    except:
        print('\nFalha na conexão com o cliente!');
        cliente.close()
        


def menuTrocas(cliente):
    enviaMsgServ('\t ========================================',cliente);
    enviaMsgServ('\t OPCOES:\t=========================',cliente);
    enviaMsgServ('\t 1:Solicitar troca                  \t=',cliente);
    enviaMsgServ('\t 2:Cadastrar cerveja                \t=',cliente);
    enviaMsgServ('\t 3:Ver sua Geladeira(Itens)         \t=',cliente);
    enviaMsgServ('\t 4:Aceitar/Recusar trocas           \t=',cliente);
    enviaMsgServ('\t 5:Kero Sair                        \t=',cliente);
    enviaMsgServ('\t ========================================',cliente);
    enviaMsgServ('\n\t = ESCOLHA UMA DAS OPCOES (EX.: 4) =\t\t=',cliente);


def boasVindas(cliente, clientesAtivos):
    enviaMsgServ('\t\t BEM VINDO AO kERO - SEU SD DE TROCAS DE CERVEJA',cliente);
    enviaMsgServ('Insira seu nome: ',cliente);
    nome = recebeMsgServ(cliente);     
    valido = autenticacao(nome.lower());
    if valido == 'T':
        try:
            while (True):
                enviaMsgServ(f' {nome}, vamos as trocas?!\n',cliente)
                transmissao(cliente, clientesAtivos, nome)
                menuTrocas(cliente)
                resp = recebeMsgServ(cliente)
                if (resp == '1'):
                    SolicitaTroca(cliente,nome)
                elif (resp == '2'):
                    CadastrarCerveja(cliente, nome)
                elif (resp == '3'):
                    listagemMeusItens(cliente, nome)
                elif (resp == '4'):
                    ListarTrocasPendentes(cliente,nome)                    
                else:
                    enviaMsgServ('Tchau!!!!',cliente)
                    return
        except:
            print('Usuario fora do Sistema!')
    else:
        enviaMsgServ(f'{nome} => Não cadastrado !!!!', cliente)
        enviaMsgServ('Deseja realizar cadastro? \n(K)ero\t(N)ao', cliente)      
        resposta = recebeMsgServ(cliente).lower();
        if (resposta == 'k'):
            cadastroUsuario(nome,cliente)
        else:            
            enviaMsgServ(f'{nome}?! Sem cadastro, sem cerveja!', cliente)
            enviaMsgServ('Voltando ao MENU PRINCIPAL ...\n', cliente)
            return           

def transmissao(cliente, clientesAtivos, nome): #verificar online
    flag=0
    trocasAtivas = database.SelectTrocas('p')
    for clienteA in clientesAtivos:
        if (clienteA == cliente):
            enviaMsgServ('\t:)\tTROCAS PENDENTES:', cliente);
            for trocas in trocasAtivas:
                if trocas[4] == nome:
                    flag = 1
                    try:
                       enviaMsgServ(f'Trocas pendentes: {trocas}', cliente);
                    except:
                        deletaCliente(clienteA,clientesAtivos);
    if(flag==0):
        enviaMsgServ(":/\tSua geladeira de TROCAS está vazia...\t:/ ",cliente);

def deletaCliente(cliente, clientesAtivos):
    clientesAtivos.remove(cliente);


####! Itens usados na parte 4####
def autenticacao(usuario):
    dadosLogin = [ ]
    
    try:
        dadosLogin = database.SelectTodosUsuarios('TPSD.db')
        cadastro = "F"
        print(usuario)
        for check in dadosLogin:
            if (check == usuario):
                cadastro = "T"
        return cadastro
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

def cadastroUsuario(nome):
    response = database.InsertUsuario('TPSD.db',nome, '1234')
    print(f'Usuario {nome} inserido com sucesso!')
    return response
    
    

def listagemDeitensTroca():
    dadosListagem = [ ]
    try:
        ##cliente.send(f'(SERVIDOR) < {nome} > Confira as cervejas disponiveis \n\tem nosso BAR'.encode('utf-8'))
        ##cliente.send(f'(SERVIDOR)[INDICE,PROPRIETARIO, CERVEJA, ABV, IBU, ESTILO]'.encode('utf-8'))
        dadosListagem = database.SelectTodasCervejas()
        if (len(dadosListagem) > 0):
            return dadosListagem
            #!MOVER PARA CLIENTE OU INTERFACE GRÁFICA
            """
            for breja in dadosListagem:
               
                if (breja[1]!=nome):
                    cliente.send(f'\n||Indice: {breja[0]} ||PROPRIETARIO: {breja[1]} ||CERVEJA: {breja[2]} ||ABV: {breja[3]} ||IBU: {breja[4]} ||ESTILO:{breja[5]} ||'.encode('utf-8'))
            cliente.send(f'\n(SERVIDOR) < {nome} > E ai?! Vai querer?'.encode('utf-8'))
            cliente.send(f'\n(SERVIDOR)[Bora] [Voltar]'.encode('utf-8'))
            
            resposta = cliente.recv(2048).decode('utf-8');
            
            if(resposta.lower() == "bora"):
                return 1
            else:
                return 0
                """
        else:
            return 404
           #cliente.send(f'\n(SERVIDOR) < {nome} >Desculpe, tente outro dia'.encode('utf-8'))
    except:
        print("Error: Sorry :/")

def listagemMeusItens(nome):
    dadosListagem = [ ]
    try:
        #cliente.send(f'(SERVIDOR) < {nome} > Essas são as cervejas que você cadastrou \n\tem nosso BAR'.encode('utf-8'))
        #cliente.send(f'(SERVIDOR)[INDICE,PROPRIETARIO, CERVEJA, ABV, IBU, ESTILO]'.encode('utf-8'))
        dadosListagem = database.SelectCervejaByUsuario(nome)
        if (len(dadosListagem) > 0):
            return dadosListagem
            """
            for breja in dadosListagem:
                cliente.send(f'\n||Indice: {breja[0]} ||PROPRIETARIO: {breja[1]} ||CERVEJA: {breja[2]} ||ABV: {breja[3]} ||IBU: {breja[4]} ||ESTILO:{breja[5]} ||'.encode('utf-8'))
            return 1       
            """ 
        else:
            #cliente.send(f'\n(SERVIDOR) < {nome} >Você não tem itens cadastrados'.encode('utf-8'))
            return 400
    except:
        print("Error: Sorry :/")
        return 400


def CadastrarCerveja(nome,cerveja):
    #cliente.send(f'\n(SERVIDOR) < {nome} > Vamos cadastrar uma cerveja'.encode('utf-8'))
    #cliente.send(f'\ndigite o nome cerveja'.encode('utf-8'))
    nomeCerveja = cerveja.nomeCerveja
    #cliente.send(f'\nAgora digite o ABV (ABV é a sigla para ALCOHOL BY VOLUME, ou quão alcoolico é um exemplar)'
    #.encode('utf-8'))
    abv = cerveja.abv
    #cliente.send(f'\nAgora digite o IBU (IBU é a sigla para International Bitterness Units, ou o quão amargo é um exemplar)'
    #.encode('utf-8'))
    ibu = cerveja.ibu
    #cliente.send(f'\nTa quaaaase! Digite agora o estilo'.encode('utf-8'))
    estilo = cerveja.estilo
    #cliente.send(f'\nConfirma as informações pra gente?'.encode('utf-8'))
    #cliente.send(f'\nnome: {nomeCerveja} ABV: {abv} IBU: {ibu} estilo:{estilo}'.encode('utf-8'))
    #cliente.send(f'\n[S] [N]'.encode('utf-8'))
    #cadastrar = cliente.recv(2048).decode('utf-8')
    database.InsertCervejaBar("TPSD.db",nome,nomeCerveja,abv,ibu,estilo)
     


def SolicitaTroca(indiceCervejaSolicit,indiceCervejaExec):
    
    try:
        #!Validar se tem itens no cliente
        dadosCervExec = database.SelectCervejaByIdBar(indiceCervejaExec)
        dadosCervSolic = database.SelectCervejaByIdBar(indiceCervejaSolicit)
        for breja in dadosCervSolic:
            solicitante = breja[1]
        for breja2 in dadosCervExec:
            executor = breja2[1]
        response = database.InsertTrocaCervejas("TPSD.db",indiceCervejaSolicit,indiceCervejaExec,solicitante,executor)
        return response
        """
        res = listagemDeitensTroca(cliente, nome)
        print("res: ",res)
        if(res == 1):
            cliente.send(f'\n(SERVIDOR) < {nome} > Escolha primeiro a cerveja que você deseja solicitar!'.encode('utf-8'))
            cliente.send(f'\n(SERVIDOR) < {nome} > É só digitar o indice da desejada'.encode('utf-8'))
            indiceExec= cliente.recv(2048).decode('utf-8');
            if(indiceExec!=0):
                cliente.send(f'\n(SERVIDOR) < {nome} > Incrivel, vou te mostrar as cervejas que você tem para oferecer numa troca!'
                .encode('utf-8'))
                tenhoItens = listagemMeusItens(cliente,nome)
                if(tenhoItens == 1):

                    cliente.send(f'\n(SERVIDOR) < {nome} > Agora só escolher o indice da cerveja que você deseja dar em troca'.encode('utf-8'))
                    indiceSolic = cliente.recv(2048).decode('utf-8');
                    dadosCervExec = database.SelectCervejaByIdBar(indiceExec)
                    dadosCervSolic = database.SelectCervejaByIdBar(indiceSolic)
                    if(indiceSolic!=0):
                        cliente.send(f'\n(SERVIDOR) < {nome} > Confirmar troca da cerveja'.encode('utf-8'))
                        for breja in dadosCervSolic:
                            solicitante = breja[1]
                            cliente.send(f'\n||Indice: {breja[0]} ||PROPRIETARIO: {breja[1]} ||CERVEJA: {breja[2]} ||ABV: {breja[3]} ||IBU: {breja[4]} ||ESTILO:{breja[5]} ||'.encode('utf-8'))
                        cliente.send(f'\n(SERVIDOR) < {nome} > Pela cerveja'.encode('utf-8'))
                        for breja2 in dadosCervExec:
                            executor = breja2[1]
                            cliente.send(f'\n||Indice: {breja2[0]} ||PROPRIETARIO: {breja2[1]} ||CERVEJA: {breja2[2]} ||ABV: {breja2[3]} ||IBU: {breja2[4]} ||ESTILO:{breja2[5]} ||'.encode('utf-8'))
                        cliente.send(f'\n(SERVIDOR) < {nome} >[Sim] [Não]'.encode('utf-8'))
                        confirm = cliente.recv(2048).decode('utf-8');

                        if(confirm.lower() == 'sim'):
                            cliente.send(f'\n(SERVIDOR) < {nome} >Troca solicitada, em breve você receberá o veredito'.encode('utf-8'))
                            database.InsertTrocaCervejas("TPSD.db",indiceSolic,indiceExec,solicitante,executor)
                            database.SelectTodasCervejas()
                
                else:
                    cliente.send(f'\n(SERVIDOR) < {nome} >Você não tem nenhuma cerveja cadastrada deseja cadastrar?'.encode('utf-8'))
                    cliente.send(f'\n(SERVIDOR) < {nome} >[S] [N]'.encode('utf-8'))
                    cadastrar = cliente.recv(2048).decode('utf-8')
                    if(cadastrar.lower() == 's'):
                        CadastrarCerveja(cliente, nome)
        """

    except:
        print("Error: Sorry :/")
        response = 400



def ListarTrocasPendentes(cliente,nome):
    trocas = database.SelectTrocas("p")
    if(len(trocas)>0):
        #enviaMsgServ(f"\tEssas são as trocas pendentes do {nome}: ", cliente)  
        trocasRes = [] 
        trocasAux = []
        for troca in trocas:
            if troca[4] == nome:
                try:
                    #!mudar para cliente
                    '''                    
                    cervejaSolict = database.SelectCervejaByIdBar(troca[1])
                    cervejaExec = database.SelectCervejaByIdBar(troca[2])

                    enviaMsgServ(f"|| Indice: {troca[0]} ||",cliente)
                    enviaMsgServ(f"|| Cerveja oferecida: {cervejaSolict} ||",cliente)
                    enviaMsgServ(f"|| Cerveja solicitada: {cervejaExec} ||",cliente)
                    '''

                    return troca
                except:
                    return 400
                    #enviaMsgServ("ops!! tivemos um problema, tente novamente mais tarde!",cliente);

"""
        enviaMsgServ("Deseja Responder alguma solicitação?",cliente)
        enviaMsgServ("[Kero(1)] [Agora não(0)]",cliente)
        resposta = recebeMsgServ(cliente)
        if(resposta == '1'):
            enviaMsgServ(f"Agora digite o indice da troca que deseja responder",cliente)
            index = recebeMsgServ(cliente)
            enviaMsgServ(f"SHOW!Agora digite se deseja realizar a troca ou rejeitar a solicitação",cliente)
            enviaMsgServ(f"[Kero(1)] [Rejeitar Solicitação(0)]",cliente)
            rej = recebeMsgServ(cliente)
            if(rej == '1'):
                try:
                    database.AtualizaTrocaCervejas("TPSD.db",index,"a")
                    enviaMsgServ(f"Troca foi aceita",cliente)
                except:
                    enviaMsgServ("ops!! tivemos um problema, tente novamente mais tarde!");
            else:
                try:
                    database.AtualizaTrocaCervejas("TPSD.db",index,"r")
                    enviaMsgServ("Ok solicitação excluida")
                except:
                    enviaMsgServ("ops!! tivemos um problema, tente novamente mais tarde!");

        else:
              enviaMsgServ("Ok retornando!!")
"""

def responderSolicitacao(resSolicitacao,indiceTroca,solic,exec):
    if(resSolicitacao == '1'):
        try:
            database.AceitaTroca("TPSD.db",indiceTroca,solic,exec)
            troca = database.SelectTrocaById(indiceTroca)
            #!generalizar depois
            database.TrocaTitularidade("TPSD.db",solic,troca[0][2])
            #enviaMsgServ(f"Troca foi aceita",cliente)
            return 200
        except:
            return 400
            #enviaMsgServ("ops!! tivemos um problema, tente novamente mais tarde!");
    else:
        try:
            database.RejeitaTroca("TPSD.db",indiceTroca,solic,exec)
            return 200
        except:
            return 400

           
     
def ListarTrocasPendentesUsr(cliente, nome):
    trocas = database.SelectTrocasByUsrExec(nome)
    if(len(trocas)>0):
        return trocas
        """
        enviaMsgServ("\tEssas são as trocas pendentes que você tem: ", cliente)
        for troca in trocas:
            cervejaSolict = database.SelectCervejaByIdBar(troca[1])
            cervejaExec = database.SelectCervejaByIdBar(troca[2])
           
            cliente.send(f'\n|| oiIndice: {troca[0]} ||CERVEJA OFERECIDA: {cervejaSolict} ||CERVEJA SOLICITADA: {cervejaExec} '.encode('utf-8'))
        """
    return 400
