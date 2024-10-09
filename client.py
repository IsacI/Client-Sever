import socket
import time

def start_client():
    host = 'localhost'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print(f'Conectado ao servidor em {host}:{port}')
    
    try:
        while True:
            client_socket.sendall(b'x' * 4096)  # Envia 4096 bytes
            time.sleep(0.01)  # Ajuste este valor para controlar a taxa de envio
    except KeyboardInterrupt:
        print('Teste interrompido.')
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
