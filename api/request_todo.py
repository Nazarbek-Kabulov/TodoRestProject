import requests

url = "http://127.0.0.1:8000/api/create-todo/"

for i in range(10):
    response = requests.post(url=url, data={
        'text': f'todo{i + 1}',
        'expires_at': '2023-11-17T12:34:56Z',
        'user': 1,
    })

response = requests.get(url=url)

print(response.content.decode())
