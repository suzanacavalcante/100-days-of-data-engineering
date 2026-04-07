import imaplib
import email
import os

from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()
print(f"DEBUG: Senha carregada tem {len(os.getenv('EMAIL_PASS', ''))} caracteres.")

# Configura as variáveis de ambiente
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')
IMAP_SERVER = os.getenv('IMAP_SERVER')

def baixar_anexos():
    if not EMAIL_USER or not EMAIL_PASS:
        print('Erro: Credenciais não encontradas no arquivo .env')
        return
    print(f'Conectando ao servidor como: {EMAIL_USER}...')

    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_USER, EMAIL_PASS)
        mail.select('inbox')

        # Busca e-mails com o assunto específico 
        status, data = mail.search(None, '(SUBJECT "Relatorio Vendas")')

        id_list = data[0].split()
        if not id_list:
            print("Nenhum e-mail novo com o assunto 'Relatorio Vendas'.")
            return
        
        latest_email_id = id_list[-1]
        status, data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)

        for part in msg.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            
            # CORREÇÃO AQUI: Content-Disposition (com 'nt')
            if part.get('Content-Disposition') is None:
                continue

            filename = part.get_filename()
            if filename:
                # Salva o anexo na pasta atual
                payload = part.get_payload(decode=True)
                with open(filename, 'wb') as f:
                    f.write(payload)
                print(f"✅ Anexo '{filename}' baixado com sucesso!")
        
        mail.logout()
    
    except Exception as e:
        print(f'Ocorreu um erro na conexão: {e}')

def diagnostico_imap():
    print(f"🔍 Iniciando diagnóstico para: {EMAIL_USER}")
    try:
        # Tentativa de conexão com o servidor
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        print("✅ Conexão com o servidor estabelecida.")

        # Tentativa de Login
        mail.login(EMAIL_USER, EMAIL_PASS)
        print("✅ Login realizado com sucesso! (O IMAP ESTÁ ATIVO)")
        
        # Tenta selecionar a Inbox
        mail.select("inbox")
        print("✅ Inbox acessada com sucesso.")
        
        mail.logout()
        print("\n🚀 Tudo certo! Você pode rodar o script de download agora.")

    except imaplib.IMAP4.error as e:
        erro = str(e)
        if "AUTHENTICATIONFAILED" in erro:
            print("\n❌ Erro de Autenticação: A senha de app ou o e-mail estão incorretos.")
        elif "IMAP lookup failed" in erro or "not enabled" in erro:
            print("\n❌ Erro de Configuração: O IMAP realmente está desativado no Gmail.")
        else:
            print(f"\n❌ Erro do IMAP: {e}")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")

if __name__ == "__main__":
    diagnostico_imap()
    baixar_anexos()
