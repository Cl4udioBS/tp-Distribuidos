import socket
import threading

#####################
# E se o servidor cair?
# Unico usuario;
# unidades sao os processos-objetos
# nao é web
#####################

HOST = 'localhost';
PORT = 7777;

clientesAtivos = [];

def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM); # ( IPV4, Protocolo TCP )
    try: 
        servidor.bind((HOST,PORT));
        servidor.listen();
        print("SERVIDOR::Ativo!\n");
    except:
        return print("SERVIDOR::Falha na inicialização!\n");

    while True:
        cliente, endereco = servidor.accept();
        clientesAtivos.append(cliente);
        thread = threading.Thread(target=tratamentoDeMensagens, args= [cliente]);
        thread.start();

def tratamentoDeMensagens(cliente):
    while True:
        try:
            msg = cliente.recv(2048);
            transmissao(msg,cliente);
        except:
            deletaCliente(cliente);
            break;


def transmissao(msg, cliente):
    for clienteA in clientesAtivos:
        if clienteA != cliente:
            try:
                clienteA.send(msg);
            except:
                deletaCliente(clienteA);

def deletaCliente(cliente):
    clientesAtivos.remove(cliente);

main();
