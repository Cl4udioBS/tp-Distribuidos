import socket
import threading
import logar

HOST = 'localhost';
PORT = 7777;

clientesAtivos = [];

#testes
cliente1 = ['ariel', '2522'];

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
            msg = logar.boasVindas(cliente);
            cliente.send(f'{ msg }'.encode('utf-8'));
            msg = cliente.recv(2048).decode('utf-8');
            print('msg:'+msg);
        except:
            deletaCliente(cliente);
            break;


def transmissao(cliente):
    for clienteA in clientesAtivos:
        if clienteA != cliente:
            try:
                clienteA.send('ping'.encode('utf-8'));
            except:
                deletaCliente(clienteA);

def deletaCliente(cliente):
    clientesAtivos.remove(cliente);

main();
