import rns
from entidades import database as db
def main():
    try: 
        print("SERVIDOR::Ativo!\n");
        rns.responderSolicitacao(1,1,"aryel","claudio")
        #print(rns.cadastroUsuario('teste7'))      
        #db.AceitaTroca("TPSD.db",1)   
        #troca = db.SelectTrocaById(1)
        #print(troca)
        #db.TrocaTitularidade("TPSD.db",troca[0][3],troca[0][2])
    except:
        return print("SERVIDOR::Falha na inicialização!\n");


if __name__ == "__main__":
    main()
