import polars as pl
import httpx
from bs4 import BeautifulSoup
import os
from datetime import datetime

def fetch_page(url: str):
    """Faz a requisição para o site e retorna o HTML bruto."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    try:
        response = httpx.get(url, headers=headers)
        response.raise_for_status()
        return response.text 
    except Exception as e:
        print(f"❌ Erro ao acessar o site: {e}")
        return None

def parse_news(html: str):
    """Extrai títulos e links usando uma lógica mais abrangente."""
    soup = BeautifulSoup(html, "lxml")
    news_list = []

    tags_titulo = soup.find_all(['h1', 'h2', 'h3'])

    for tag in tags_titulo:
        link_element = tag.find('a') 
        if link_element:
            title = link_element.get_text(strip=True)
            link = link_element.get('href')
            
            if link and link.startswith('/'):
                link = f"https://www.infomoney.com.br{link}"

            if title and len(title) > 10: 
                news_list.append({
                    "titulo": title,
                    "url": link,
                    "data_extracao": datetime.now()
                })
    
    return news_list

def save_news(data: list):
    """Converte para Polars e salva os arquivos."""
    if not data:
        print("Nenhum dado encontrado para salvar.")
        return

    df = pl.DataFrame(data)
    
    output_dir = "data" 
    
    os.makedirs(output_dir, exist_ok=True)
    
    df.write_parquet(f"{output_dir}/noticias_infomoney.parquet")
    df.write_csv(f"{output_dir}/noticias_infomoney.csv")
    
    print(f"{len(df)} notícias extraídas e salvas com sucesso!")
    print(df.head(5))
    
if __name__ == "__main__":
    print("Iniciando Web Scraping de Notícias...")
    URL_TARGET = "https://www.infomoney.com.br/mercados/"
    
    html_content = fetch_page(URL_TARGET)
    if html_content:
        news_data = parse_news(html_content)
        save_news(news_data)
