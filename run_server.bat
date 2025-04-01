@echo off
echo Iniciando o servidor...

REM Verifica se o Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo Python nao encontrado! Por favor, instale o Python 3.x
    pause
    exit /b 1
)

REM Instala as dependências
echo Instalando dependencias...
pip install -r requirements.txt

REM Verifica se o certificado SSL existe
if not exist server.pem (
    echo Gerando certificado SSL...
    openssl req -x509 -newkey rsa:4096 -keyout server.pem -out server.pem -days 365 -nodes -subj "/CN=localhost"
)

REM Executa o servidor
echo Iniciando o servidor...
python server.py

pause 