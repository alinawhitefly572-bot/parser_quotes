from config import BASE_URL, OUTPUT_DIR
from parser import get_quotes
from exporter import save_to_docx, save_to_csv

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    print("Сбор данных...")
    quotes = get_quotes(BASE_URL)
    
    print(f"Собрано {len(quotes)} цитат. Сохраняем...")
    
    save_to_docx(quotes, OUTPUT_DIR / 'quotes.docx')
    save_to_csv(quotes, OUTPUT_DIR / 'quotes.csv')
    
    print("Готово!")

if __name__ == '__main__':
    main()