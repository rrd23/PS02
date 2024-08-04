#Создайте словарь с данными для отправки (например, {'title': 'foo', 'body': 'bar', 'userId': 1}).

import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

response = requests.post(url, json=data)

print(response.status_code)


print(f"ответ: {response.json()}")