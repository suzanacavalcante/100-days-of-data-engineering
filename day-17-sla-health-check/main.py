import os
import time

from datetime import datetime, timedelta

class HealthCheck:
    def __init__(self, log_dir: str, sla_hours: int = 24):
        self.log_dir = log_dir
        self.sla_limit = timedelta(hours=sla_hours)

    def check_jobs(self):
        print(f'{"="*40}')
        print(f'MONITOR DE SAÚDE - {datetime.now().strftime("%d/%m %H:%M")}')
        print(f'{"="*40}')

        # Lista todos os arquivos no diretório de logs
        files = os.listdir(self.log_dir)

        # Filtra os jobs únicos baseados nos nomes dos arquivos
        jobs = set(f.split('.')[0] for f in files if '.' in f)

        for job in jobs:
            success_file = os.path.join(self.log_dir, f'{job}.success')
            error_file = os.path.join(self.log_dir, f'{job}.error')

            # 1. Checa Falha Crítica
            if os.path.exists(error_file):
                with open(error_file, 'r') as f:
                    last_error = f.readlines()[-1].strip()
                print(f'{job.upper()}: FALHA DETECTADA!')
                print(f'Erro: {last_error}')

            # 2. Checa SLA (Atraso)
            elif os.path.exists(success_file):
                mtime = datetime.fromtimestamp(os.path.getmtime(success_file))
                if datetime.now() - mtime > self.sla_limit:
                    print(f'{job.upper()}: FORA DO SLA (Última sucesso: {mtime})')
                else:
                    print(f'{job.upper()}: SAUDÁVEL')
            
            else:
                print(f'{job.upper()}: STATUS DESCONHECIDO')

if __name__ == '__main__':
    LOG_PATH = 'logs'
    if not os.path.exists(LOG_PATH):
        os.makedirs(LOG_PATH)

    monitor = HealthCheck(log_dir=LOG_PATH, sla_hours=2)
    monitor.check_jobs()