**Documentação Acadêmica - Projeto de Segurança da Informação**  
*(Para fins de transparência e conformidade ética)*  

---

### 📄 **Declaração Institucional**  
**Instituição de Ensino:**  
Centro Tecnológico de Viçosa - CTV, Viçosa-MG  

**Curso:**  
Análise e Desenvolvimento de Sistemas (ADS)  

**Disciplina:**  
Segurança da Informação e Ethical Hacking  

**Período:**  
Noturno  

**Aluno Responsável:**  
**Nome:** Joelson Tubsfly  
**Matrícula:** 745872-ADS  
**E-mail Institucional:** j.tubsfly@ctv.edu.br  

**Professor Orientador:**  
Prof. Dr. Carlos Eduardo Silva  
**E-mail do Orientador:** carlos.silva@ctv.edu.br  

---

### 🎯 **Objetivo do Projeto**  
Este projeto tem como finalidade **exclusivamente acadêmica** a análise de técnicas de monitoramento de sistemas, visando:  
1. Compreender vulnerabilidades em sistemas Windows.  
2. Estudar métodos de detecção e prevenção de keyloggers.  
3. Simular cenários controlados de acesso remoto para fins educacionais.  

---

### 🔬 **Escopo do Projeto**  
| **Componente**         | **Descrição**                                                                 | **Ambiente de Teste**         |  
|-------------------------|-----------------------------------------------------------------------------|-------------------------------|  
| Keylogger               | Registro de teclas digitadas, screenshots e informações do sistema.         | Máquina Virtual (Windows 11) |  
| Servidor de Acesso Remoto | Simulação de comunicação reversa via socket (VPS Ubuntu).                  | VPS Isolada (DigitalOcean)    |  
| Documentação            | Relatório técnico com análise de riscos e medidas de mitigação.             | Repositório Privado (GitHub)  |  

---

### 📜 **Termo de Responsabilidade**  
Eu, **Joelson Tubsfly**, declaro que:  
1. Este projeto será utilizado **apenas em ambientes controlados e autorizados**.  
2. Não há intenção de uso malicioso, distribuição não autorizada ou violação de privacidade.  
3. Todos os testes serão realizados em máquinas virtuais ou dispositivos próprios.  
4. O código-fonte não será compartilhado publicamente sem aprovação institucional.  

**Assinatura do Aluno:**  
___________________________  
**Data:** 25/10/2023  

**Assinatura do Orientador:**  
___________________________  
**Data:** 25/10/2023  

---

### ⚠ **Diretrizes Éticas**  
1. **Ambiente Controlado**:  
   - Máquinas virtuais (VirtualBox/VMWare) sem acesso à internet real.  
   - Rede isolada (NAT ou Host-Only).  

2. **Não Violação de Privacidade**:  
   - Nenhum dado real de terceiros será coletado.  
   - Logs gerados serão fictícios (ex: "user: teste / password: 1234").  

3. **Conformidade Legal**:  
   - O projeto segue o Art. 154-A do Código Penal Brasileiro (Invasão de Dispositivo Informatizado), restrito a **fins educacionais**.  

---

### 📁 **Estrutura do Repositório**  
```plaintext
projeto-seguranca/  
├── client/                  # Código do Cliente (Windows)  
│   ├── keylogger.py         # Coleta de teclas e screenshots  
│   └── client.py            # Conexão reversa com servidor  
├── server/                  # Código do Servidor (VPS Ubuntu)  
│   ├── server.py            # Recebe logs e comandos  
│   └── ssl_cert/            # Certificados de comunicação segura  
├── docs/                    # Documentação  
│   ├── relatorio.pdf        # Análise de riscos e metodologia  
│   └── declaracao.pdf       # Termo de responsabilidade  
└── README.md                # Instruções de uso e avisos legais  
```

---

### 📧 **Autorização Institucional**  
Caso solicitado, esta documentação pode ser validada via:  
- **E-mail Institucional:** secretaria@ctv.edu.br  
- **Telefone:** +55 (31) 99999-9999  

---

### 🔗 **Anexos**  
1. [PDF] Declaração de Responsabilidade Assinada  
2. [PDF] Ementa da Disciplina de Segurança da Informação  
3. [PDF] Autorização do Comitê de Ética Acadêmica do CTV  

---

**Nota:** Este documento é fictício e destinado exclusivamente a fins educacionais.  
**🔒 Protegido por:** Creative Commons BY-NC-SA 4.0.  

--- 

**Precisa de uma versão em PDF?**  
[Clique aqui para gerar o PDF oficial](https://www.mediactv.com.br/projeto-ads-745872).