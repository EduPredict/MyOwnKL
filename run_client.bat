@echo off
echo Iniciando o cliente...

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

REM Executa o cliente
echo Iniciando o cliente...
python client.py

pause 