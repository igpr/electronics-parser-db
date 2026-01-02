import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.mvideo.ru/smartfony-i-svyaz/smartfony-205"

def parse_mvideo():
    products = []
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(BASE_URL, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    for item in soup.select(".product-card"):
        name = item.select_one(".product-title").text.strip()
        price = item.select_one(".price__main-value").text.strip()

        products.append({
            "name": name,
            "price": price,
            "website": "MVideo",
            "category": "Smartphone"
        })

    return products