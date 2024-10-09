import socket

def start_server():
    host = '0.0.0.0'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f'Servidor escutando em {host}:{port}...')
    while True:
        conn, addr = server_socket.accept()
        print(f'Conexão de {addr}')
        conn.close()

if __name__ == "__main__":
    start_server()
