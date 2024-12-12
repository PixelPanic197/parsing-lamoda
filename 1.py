import requests
from bs4 import BeautifulSoup

# Заголовок для имитации браузера
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

# Базовый URL с placeholder для номера страницы
base_url = "https://www.lamoda.ru/b/23751/brand-modis/?sitelink=cross_link&page={}"

# Список для хранения идентификаторов товаров
product_ids = []

# Обход страниц с 1 по 21
for page in range(1, 22):
    url = base_url.format(page)
    response = requests.get(url, headers=headers)

    # Проверяем успешность запроса
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Находим все элементы с классом x-product-card__link x-product-card__hit-area
        links = soup.find_all('a', class_='x-product-card__link x-product-card__hit-area')

        for link in links:
            href = link.get('href', '')
            if href:
                # Извлекаем только идентификатор товара
                product_id = href.split('/')[2]
                product_ids.append(product_id)
    else:
        print(f"Ошибка запроса на странице {page}: {response.status_code}")

# Вывод итогового списка
print(product_ids)
