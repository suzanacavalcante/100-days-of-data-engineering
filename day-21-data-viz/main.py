import csv

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich import print

class WeatherDashboard:
    def __init__(self, file_path):
        self.file_path = file_path
        self.console = Console()
    
    def load_data(self):
        data = []
        try:
            with open(self.file_path, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    data.append(row)
            return data
        
        except FileNotFoundError:
            self.console.print("[bold red]❌ Erro:[/bold red] Arquivo 'historico_climatico.csv' não encontrado!")
            return []
        
    def display(self):
        records = self.load_data()
        if not records:
            return
        
        # Criando a Tabela
        table = Table(title="🌦️ Histórico Climático - Últimas 24h", title_style="bold magenta")

        table.add_column('Horário', style='cyan', no_wrap=True)
        table.add_column('Temp (°C)', justify='right', style='yellow')
        table.add_column('Umidade (%)', justify='right', style='blue')
        table.add_column('Chuva (%)', justify='right', style='green')

        # 10 últimos registros
        for row in records[-10:]:
            temp = float(row['temperatura_c'])
            temp_color = "[red]" if temp > 25 else "[cyan]"

            table.add_row(
                row['timestamp'],
                f"{temp_color}{row['temperatura_c']}°C[/]", 
                f"{row['umidade_relativa']}%",
                f"{row['prob_precipitacao']}%"
            )

        # Criando um Painel de Resumo 
        resumo = f"""
            [bold]Localização:[/] Osasco/São Paulo
            [bold]Total de Registros:[/] {len(records)}
            [bold]Status do Pipeline:[/] [green]Online[/]
        """

        self.console.print(Panel(resumo, title="[bold white]Informações do Sistema[/]", border_style="bright_blue"))
        self.console.print(table)

if __name__ == '__main__':
    dash = WeatherDashboard('../day-20-historico-climatico/historico_climatico.csv')
    dash.display()