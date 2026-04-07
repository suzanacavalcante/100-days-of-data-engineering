# 📧 Day 12: Email Attachment Downloader

O décimo segundo dia resolve um problema clássico de integração: a ingestão de dados via e-mail. Criamos um robô de captura automática para bases de dados enviadas por parceiros.

## 🎯 Objetivo
Automatizar a conexão com servidores de e-mail via protocolo IMAP, realizar o parsing de mensagens multipart e extrair anexos CSV/Excel para a camada de processamento local.

## 🛠️ Stack Técnica
- **Protocolo:** `IMAP4_SSL`
- **Parsing:** `email.message`, `imaplib`
- **Automação:** Gerenciamento de fluxos de download e I/O.

## 🏗️ Fluxo de Automação
1. **Handshake:** Autenticação segura com o servidor de e-mail.
2. **Search Logic:** Filtragem de mensagens por critérios (Assunto/Remetente).
3. **Payload Extraction:** Decodificação de base64 e salvamento de binários (anexos).

## 🛠️ Configuração de Segurança e Ambiente
Para que este script funcione com o Gmail, é necessário seguir dois passos críticos de segurança: a geração de uma Senha de App e a proteção de dados via Variáveis de Ambiente.

**Gerar Senha de App no Google (Gmail):**
1. Acesse sua Conta Google e vá em Segurança.
2. Certifique-se de que a Verificação em duas etapas esteja ATIVADA.
3. Pesquise por "Senhas de app" na barra de busca superior ou acesse o menu de Verificação em duas etapas e role até o final.
4. Dê um nome ao app (ex: Python Data Engineering) e clique em Criar.
5. IMPORTANTE: O Google exibirá uma senha de 16 caracteres (ex: abcd efgh ijkl mnop). Copie-a exatamente assim, mas remova os espaços ao colar no seu .env.

**Configurar o Arquivo .env**
Nunca coloque suas credenciais diretamente no código (main.py). Usamos o arquivo .env para manter esses dados protegidos e fora do controle de versão (Git).

1. Na raiz do seu projeto, crie um arquivo chamado .env (sem nome antes do ponto).
2. Adicione as seguintes variáveis dentro dele:
```bash
    EMAIL_USER=seu_email@gmail.com
    EMAIL_PASS=suasenha de16caracteressemespaços
    IMAP_SERVER=imap.gmail.com
```
3. Segurança extra: Crie um arquivo .gitignore e adicione a linha .env dentro dele. Isso garante que, ao fazer o git push, suas senhas não sejam enviadas para o repositório público.