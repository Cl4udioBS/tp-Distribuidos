import socket
import threading
import rns
from entidades import cliente as c

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
            rns.boasVindas(cliente);
            #cliente.send(f'{ msg }'.encode('utf-8'));
            c.recebeMensagens(cliente);

        except:
            deletaCliente(cliente);
            break;


def transmissao(cliente): #verificar online
    for clienteA in clientesAtivos:
        if clienteA != cliente:
            try:
                clienteA.send('ping'.encode('utf-8'));
            except:
                deletaCliente(clienteA);

def deletaCliente(cliente):
    clientesAtivos.remove(cliente);


main();
