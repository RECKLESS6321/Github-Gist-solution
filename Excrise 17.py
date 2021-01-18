import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
soup = BeautifulSoup(r.text, features = "html.parser")

a = [headline.get_text(strip=True) for headline in soup.select(':is(h1, h2, h3, h4, h5, h6)')][3:-4]
print(f"\n{a}")