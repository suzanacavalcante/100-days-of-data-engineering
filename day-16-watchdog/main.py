import time 
import os 

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MeuHandler(FileSystemEventHandler):
    # Dispara quando um novo arquivo aparece
    def on_created(self, event):
        if not event.is_directory:
            filename = os.path.basename(event.src_path)
            print(f'Novo arquivo detectado: {filename}')

            if filename.endswith('.csv'):
                print(f'Processando o arquivo CSV: {filename}...')
            else:
                print(f'O arquivo {filename} não é um CSV. Ignorando...')

def iniciar_monitoramento(caminho_da_pasta):
    print(f'Vigiando a pasta: {caminho_da_pasta}')

    # Cria a pasta se ela não existir
    if not os.path.exists(caminho_da_pasta):
        os.makedirs(caminho_da_pasta)

    event_handler = MeuHandler()
    observer = Observer()
    observer.schedule(event_handler, caminho_da_pasta, recursive=False)

    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print('\nMonitoramento encerrado')
    observer.join()

if __name__ == "__main__":
    iniciar_monitoramento("./input_dados")