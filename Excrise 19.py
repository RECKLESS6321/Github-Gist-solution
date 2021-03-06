import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")
page = BeautifulSoup(url.text, 'html.parser')

print(*[p.get_text() for p in page.select('article.article.main-content p')], sep = '\n')