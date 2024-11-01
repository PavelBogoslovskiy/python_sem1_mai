# Виртуальное окружение готово, но заливать его на гит как-то не хочется, поэтому 
# просто приложу скрины, подтверждающие его наличие
# Пример url в задании не отображается, поэтому я взял другой
import requests
from bs4 import BeautifulSoup

# Выполнение запроса на url
url = "https://en.wikipedia.org/wiki/Main_Page"
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    print("Успешное подключение к сайту")
    #  Парсинг HTML-кода
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    # Извлекаем заголовок
    headings = soup.find_all('h1')
    for heading in headings:
        print(heading.text)

else:
    print(f"Ошибка при подключении. Код ошибки: {response.status_code}")


