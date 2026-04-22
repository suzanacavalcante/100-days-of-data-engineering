import os
import zipfile
from datetime import datetime
from pathlib import Path

class BackupManager:
    def __init__(self, source_dir: str, backup_dir: str, keep_last: int = 3):
        # Resolve o caminho relativo para absoluto para evitar erro de diretório
        self.source_path = Path(source_dir).resolve()
        self.backup_path = Path(backup_dir).resolve()
        self.keep_last = keep_last
        
        self.backup_path.mkdir(parents=True, exist_ok=True)

    def _rotate_backups(self):
        backups = sorted(
            list(self.backup_path.glob("backup_*.zip")),
            key=lambda x: x.stat().st_mtime,
            reverse=True
        )

        if len(backups) > self.keep_last:
            print(f"Rotacionando: Mantendo apenas os {self.keep_last} mais recentes.")
            for old_backup in backups[self.keep_last:]:
                old_backup.unlink()
                print(f"🗑️ Removido: {old_backup.name}")

    def create_backup(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        zip_name = f"backup_{timestamp}.zip"
        zip_full_path = self.backup_path / zip_name

        # Validação de segurança
        if not self.source_path.exists():
            print(f"Erro: O diretório {self.source_path} não foi encontrado.")
            return

        print(f"Iniciando backup total de: {self.source_path}")
        
        files_found = 0
        with zipfile.ZipFile(zip_full_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in self.source_path.rglob('*'):
                if file.is_file():
                    print(f"  📄 Adicionando: {file.name}")
                    zipf.write(file, arcname=file.relative_to(self.source_path))
                    files_found += 1
        
        if files_found > 0:
            print(f"Backup concluído! {files_found} arquivos compactados em: {zip_name}")
            self._rotate_backups()
        else:
            zip_full_path.unlink()
            print("Nenhum arquivo encontrado para backup. Operação cancelada.")

if __name__ == '__main__':
    manager = BackupManager(
        source_dir='../day-17-sla-health-check/logs',
        backup_dir='backups',
        keep_last=3
    )
    manager.create_backup()