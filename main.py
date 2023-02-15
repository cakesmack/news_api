import requests
from send_email import send_email
from credentials import api

api = api

topic = 'guitar'

url = 'https://newsapi.org/v2/everything?'\
    f'q={topic}'\
    '&from=2023-01-15'\
    '&sortBy=publishedAt'\
    f'&apiKey={api}'\
    '&language=en'

r = requests.get(url)

page = r.json()

content = page['articles']


body = f'Subject: Todays {topic} News'

for i in content[:20]:
    title = i['title']
    author = i['author']
    date = i['publishedAt']
    link = i['url']
    body = body + f'''

    {title}

    Published By - {author} on {date}
    {link}
    *****

    '''
body = body.encode('utf-8')
send_email(message=body)







