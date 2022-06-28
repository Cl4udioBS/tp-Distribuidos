import socket
import threading


HOST = 'localhost';
PORT = 7777;


def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

    try: 
        cliente.connect((HOST, PORT));
    except:
        return print("Conexão indisponível...");

    usuario = input('Usuario -> ');
    print(usuario +'- STATUS: Conectado.');

    #threads:
    thread1 = threading.Thread(target=recebeMensagens, args = [ cliente ]);
    thread2 = threading.Thread(target=enviaMensagens, args = [ cliente, usuario ]);

    thread1.start();
    thread2.start();

def recebeMensagens(cliente):
    while True:
        try:
            msg = cliente.recv(2048).decode('utf-8'); #socket transmite em bytes
            print(msg+'\n');
        except:
            print('\nFalha na conexão com o servidor!');
            print('<Enter> para sair');
            cliente.close();
            print('STATUS: Desconectado.'); ## ????????????????
            break;

def enviaMensagens(cliente, usuario):
    while True:
        try:
            msg = input('\n');
            cliente.send(f'<{usuario}> {msg}'.encode('utf-8'));
        except:
            print('Falha no envio!\n');
            return;


main();