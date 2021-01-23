import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.nytimes.com/")
soup = BeautifulSoup(url.text, "html.parser")

with open(str(input("Please enter a file name: ")), "w") as f:
    for i in soup.find_all('p'):
        if i.a: 
            f.write(i.a.text.replace("\n", " ").strip())
        else: 
            f.write(i.contents[0].strip())
    