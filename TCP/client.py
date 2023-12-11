import socket
import threading

def main():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try: 
        client_socket.connect(('127.0.0.1', 11505))  #cria a conexão com o servidor
    
    except:
        return print('\n Servidor não conectado')   #Para caso o servidor já esteja aberto
    
    usuario = input('\nUsuario: ')
    print(f'<{usuario}> conectado com sucesso')

    threadRecebe = threading.Thread(target=recebeMensagem, args=[client_socket])
    threadEnvia = threading.Thread(target=enviaMensagem, args=[client_socket, usuario])  #para que possa rodar simultaneamente

    threadRecebe.start()
    threadEnvia.start()


def recebeMensagem(client_socket):
    while True:
        try:
            mensagem = client_socket.recv(2048).decode('utf-8')
            print(mensagem+'\n')
        
        except:
            print('\n Não foi possível enviar a mensagem') #precisa apertar enter pra contiunuar 
            client_socket.close()
            break

def enviaMensagem(client_socket, usuario):
    while True:
        try:
            mensagem = input('\n')
            client_socket.send(f'<{usuario}>: {mensagem}'.encode('utf-8'))
        
        except:
            return 
        
main()