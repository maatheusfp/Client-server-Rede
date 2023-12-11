import socket
import threading

clientes = [] #os clientes ficam armazenados em uma lista para poder realizar as funções

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_socket.bind(('127.0.0.1', 11505))
        server_socket.listen() #colocando um número dentro da função posso limitar a quantidade de conexões
        print('\nServidor em funcionamento')

    except:
        return print('\n Servidor ja em uso')
    
    while True:
        cliente = server_socket.accept() #aceitar as requisições os clientes
        clientes.append(cliente) 

        threadServer = threading.Thread(target=recebeMensagem, args=[cliente])
        threadServer.start()
        
def recebeMensagem(cliente):
    while True:
        try:
            mensagem = cliente.recv(2048)
            transmissão(mensagem, cliente)
        except:
            clientes.remove(cliente)  #aqui ele não está mais conectado, por isso o break
            break

def transmissão(mensagem, cliente):    #essa função manda a mensagem de um cliente para todos os outros
    for i in clientes:
        if i != cliente:
            try:
                i.send(mensagem) 
                print('\nMensagem enviada com sucesso')    
            
            except:
                print('\n Mensagem não enviada')
                clientes.remove(cliente)  #caso não consiga mais mandar mensagem, remove ele da lista


main() 