class TrocaCerveja:
    def __init__(self):
        self.__listaCervejasTroca = []
        self.__listaUsuarios = []

##! vai se perder se der pop
    def AdicionarCervejaTroca(self,nomeCerveja, usuario):
        self.__listaCervejasTroca.append(nomeCerveja)
        self.__listaUsuarios.append(usuario)

    def ListarCervejasTroca(self):
        print("Cervejas para troca")
        qtdCervejas = len(self.__listaCervejasTroca)
        for i in range (qtdCervejas):
            print(self.__listaCervejasTroca[i])
            print(self.__listaUsuarios[i])