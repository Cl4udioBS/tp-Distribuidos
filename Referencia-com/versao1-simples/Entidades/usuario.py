import Cerveja
import TrocaCerveja
class Usuario():

    def __init__(self, nome, senha):
        self.__nome = nome
        self.__senha = senha
        self.__geladeira = []##lista de cervejas que o usuario tem
    
    def get_geladeira(self):
        return self.__geladeira

    def CadastrarItem(self, nome,ABV, IBU, estilo, quantidade):
        cerveja = Cerveja.Cerveja(nome,ABV, IBU, estilo, quantidade)
        print("geladeira: ", self.get_geladeira())
        if nome.upper() in self.__geladeira:
            print("item ja adicionado\n")
        
        else:
            self.__geladeira.append(cerveja)
            print("geladeira: ", self.get_geladeira())
    
  




        
       

##*Main só pra teste, mover para um geral com os sockets depois
if __name__ == "__main__":
    usr = Usuario("aryel", "2533")
    cerveja1 = Cerveja.Cerveja("orval","7%",15,"belgian dark strong ale",4)
    AmbienteTrocas = TrocaCerveja.TrocaCerveja()
    print("main: ",cerveja1.get_nome() )
    
  
    usr.CadastrarItem(cerveja1.get_nome(), cerveja1.get_ABV(), cerveja1.get_IBU(), cerveja1.get_estilo(), cerveja1.get_quantidade())
    AmbienteTrocas.AdicionarCervejaTroca("orval", "aryel")
    AmbienteTrocas.AdicionarCervejaTroca("guinnes", "claudio")
    AmbienteTrocas.ListarCervejasTroca()