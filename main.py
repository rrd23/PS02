import requests
import pprint

# URL-адрес API GitHub для поиска репозиториев
url = "https://api.github.com/search/repositories"

# Параметры запроса для поиска репозиториев с кодом HTML
params = {"q": "language:html"}

# Отправка GET-запроса
response = requests.get(url, params=params)

# Вывод статуса-кода ответа
print("Статус-код ответа:", response.status_code)

# Вывод содержимого ответа в формате JSON
print("Содержимое ответа:")
pprint.pprint(response.json())
print(f"количество репозиториев: {response.json()['total_count']}")