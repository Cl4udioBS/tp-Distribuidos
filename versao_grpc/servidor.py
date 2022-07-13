import socket
import threading
import rns
from entidades import cliente as c
from entidades import database as db
HOST = 'localhost';
PORT = 7777;

clientesAtivos = [];

def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM); # ( IPV4, Protocolo TCP )
    try: 
        servidor.bind((HOST,PORT));
        servidor.listen();
        print("SERVIDOR::Ativo!\n");
        db.InicializaBD()
        
    except:
        return print("SERVIDOR::Falha na inicialização!\n");

    while True:
        cliente, endereco = servidor.accept();
        clientesAtivos.append(cliente);
        thread = threading.Thread(target=tratamentoDeMensagens, args= [cliente, clientesAtivos]);
        thread.start();
        print("Clientes Online:\n",clientesAtivos)

def tratamentoDeMensagens(cliente,clientesAtivos):
    while True:
        try:
            rns.boasVindas(cliente, clientesAtivos);
        except:
            rns.deletaCliente(cliente, clientesAtivos);
            break;


main();
