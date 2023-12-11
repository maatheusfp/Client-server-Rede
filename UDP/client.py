import socket
import threading

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        usuario = input('\nUsuario: ')
        client_socket.sendto(usuario.encode('utf-8'), ('127.0.0.1', 11505))
        print(f'<{usuario}> Conectado com Sucesso')

        threadRecebe = threading.Thread(target=recebeMensagem, args=[client_socket])
        threadEnvia = threading.Thread(target=enviaMensagem, args=[client_socket, usuario])

        threadRecebe.start()
        threadEnvia.start()

        threadRecebe.join()
        threadEnvia.join()

    except Exception as e:
        print(f'\nErro ao conectar ao servidor: {e}')
    finally:
        client_socket.close()

def recebeMensagem(client_socket):
    while True:
        try:
            mensagem, endereco_servidor = client_socket.recvfrom(2048)
            print(mensagem.decode('utf-8') + '\n')
        except:
            print('\nNão foi possível receber a mensagem')
            break

def enviaMensagem(client_socket, usuario):
    while True:
        try:
            mensagem = input('\n')
            mensagem_formatada = f'<{usuario}>: {mensagem}'
            client_socket.sendto(mensagem_formatada.encode('utf-8'), ('127.0.0.1', 11505))
        except:
            print('\nNão foi possível enviar a mensagem')
            break
        
main()