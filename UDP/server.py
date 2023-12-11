import socket
import threading
import datetime

clientes = []

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        server_socket.bind(('127.0.0.1', 11505))
        print('\nServidor em funcionamento')
    except Exception as e:
        print(f'\nErro ao vincular: {e}')
        return

    while True:
        mensagem, endereco_cliente = server_socket.recvfrom(2048)

        if endereco_cliente not in clientes:
            clientes.append(endereco_cliente)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} - Cliente {endereco_cliente}: {mensagem.decode('utf-8')}\n")

        # Iniciar uma thread para lidar com a mensagem de um cliente
        threadServer = threading.Thread(target=trataMensagem, args=(mensagem, endereco_cliente, server_socket))
        threadServer.start()

def trataMensagem(mensagem, endereco_cliente, server_socket):
    for cliente in clientes:
        if cliente != endereco_cliente:
            try:
                server_socket.sendto(mensagem, cliente)
            except Exception as e:
                print(f'\nErro ao enviar mensagem para {cliente}: {e}')

main()
