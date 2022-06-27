class Cerveja:
    def __init__(self,nome,ABV, IBU, estilo, quantidade):
        self.__nome= nome
        self.__ABV = ABV
        self.__IBU = IBU
        self.__estilo = estilo
        self.__quantidade = quantidade
    
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome
    

    def set_abv(self, abv):
        self.__abv = abv
    
    def get_ABV(self):
        return self.__ABV
    

    def set_ibu(self, ibu):
        self.__ibu = ibu

    def get_IBU(self):
        return self.__IBU


    def set_estilo(self, estilo):
        self.__estilo = estilo
    
    def get_estilo(self):
        return self.__estilo

    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade
    
    def get_quantidade(self):
        return self.__quantidade

