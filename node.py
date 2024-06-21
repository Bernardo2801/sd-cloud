import socket
import os

def register_files(server_ip, server_port):
    files = os.listdir('./a/node')  # Lista os arquivos no diretório atual
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, server_port))
        command = f"REGISTER {' '.join(files)}"
        s.sendall(command.encode())
        print(f"Arquivos registrados: {files}")

if __name__ == "__main__":
    server_ip = '127.0.0.1'
    server_port = 65432
    register_files(server_ip, server_port)
