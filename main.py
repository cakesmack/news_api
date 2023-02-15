import requests

api_key = '0eab0885700542848bfb89d93c279600'
url = 'https://newsapi.org/v2/everything?q=tesla&from=2023-01-15&sortBy=publishedAt&apiKey=0eab0885700542848bfb89d93c279600'

r = requests.get(url)
page = r.json()

content = page['articles']


for i in content:
    print(i['title'])






