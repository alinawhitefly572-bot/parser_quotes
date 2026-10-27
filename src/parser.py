import requests
from bs4 import BeautifulSoup

def get_quotes(url: str) -> list[dict]:
    response = requests.get(url)
    response.raise_for_status() # Проверка на ошибки (404, 500)
    soup = BeautifulSoup(response.text, 'lxml')
    
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    tags = soup.find_all('div', class_='tags')
    
    data = []
    for i in range(len(quotes)):
        tagsforquote = tags[i].find_all('a', class_='tag')
        data.append({
            'Текст': quotes[i].text,
            'Автор': authors[i].text,
            'Теги': ', '.join([t.text for t in tagsforquote])
        })
    return data