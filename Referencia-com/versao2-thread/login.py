class Usuario():

    def __init__(self, nome, senha):
        self.__nome = nome
        self.__senha = senha


def boasVindas(cliente):
    cliente.send('\t\t BEM VINDO AO kERO - SEU SD DE TROCAS DE CERVEJA\n'.encode('utf-8'));
    cliente.send('Insira seu nome: '.encode('utf-8'));
    nome = cliente.recv(2048).decode('utf-8');
    cliente.send('Insira sua senha:'.encode('utf-8'));
    senha = cliente.recv(2048).decode('utf-8');
    usuario = Usuario(nome,senha);   
    return usuario;