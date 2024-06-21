import socket
import threading
import time

# Dicionário para armazenar os arquivos disponíveis em cada node
nodes_files = {}

# Função para lidar com as conexões dos nodes
def handle_node_connection(conn, addr):
    print(f"Conexão estabelecida com {addr}")
    node_ip = addr[1]
    try:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            command, *params = data.split()
            if command == "REGISTER":
                # Registrar os arquivos disponíveis do node
                files = params
                nodes_files[node_ip] = files
                print(f"Arquivos registrados do node {node_ip}: {files}")
                display_files()
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        conn.close()
        if node_ip in nodes_files:
            del nodes_files[node_ip]
        print(f"Conexão com {addr} encerrada")

def display_files():
    while True:
        print("Arquivos registrados por cada node:")
        for node_ip, files in nodes_files.items():
            print(f"{node_ip}: {', '.join(files)}")
        print("\n")
        time.sleep(5)  # Atualiza a cada 5 segundos

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 65432))
    server_socket.listen(5)
    print("Servidor BORDER está rodando...")

    while True:
        conn, addr = server_socket.accept()
        d = threading.Thread(target=handle_node_connection, args=(conn, addr))
        d.start()

if __name__ == "__main__":
    main()
