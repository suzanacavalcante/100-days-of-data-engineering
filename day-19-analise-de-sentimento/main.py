import string
import csv
import os

from textblob import TextBlob

class SentimentAnalyzer:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.results = {
            'Positivo': 0,
            'Negativo': 0,
            'Neutro': 0
        }
    
    def clean_text(self, text):
        """
        Sanitização: converte para minúsculas e remove pontuação
        """
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        return text.strip()
    
    def _print_summary(self):
        total = sum(self.results.values())
        print(f"\n{'='*60}")
        print(f'RESUMO ESTATÍSTICO ({total} feedbacks):')
        for k, v in self.results.items():
            pct = (v / total) * 100 if total > 0 else 0
            print(f'{k}: {v} ({pct:.1f}%)')
        print(f"\n{'='*60}")

    def process_feedbacks(self):
        if not os.path.exists(self.file_path):
            print(f'Erro: Arquivo {self.file_path} não encontrado.')
            return
        
        print(f"{'='*60}")
        print("PIPELINE DE ANÁLISE DE SENTIMENTOS - DIA 19")
        print(f"{'='*60}")

        with open(self.file_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                feedback = row['texto']
                cleaned = self.clean_text(feedback)

                # Análise usando TextBlob
                blob = TextBlob(cleaned)
                try:
                    # O texto deve ser traduzido para aumentar a precisão, pois o idioma nativo do TextBlob é inglês
                    en_blob = blob.translate(from_lang='pt', to='en')
                    polarity = en_blob.sentiment.polarity
                except:
                    polarity = blob.sentiment.polarity

                # Classificação do Score
                if polarity > 0.1:
                    sentiment = 'Positivo'
                elif polarity < -0.1:
                    sentiment = 'Negativo'
                else:
                    sentiment = 'Neutro'
                
                self.results[sentiment] += 1
                print(f'[{sentiment[:3]}] - {feedback[:55]}...')

        self._print_summary()

if __name__ == '__main__':
    analyzer = SentimentAnalyzer('feedbacks.csv')
    analyzer.process_feedbacks()