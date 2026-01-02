import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.eldorado.ru/c/smartfony/"

def parse_eldorado():
    products = []
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(BASE_URL, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    for item in soup.select("li.product-card"):
        name = item.select_one(".product-card__title").text.strip()
        price = item.select_one(".product-card__price").text.strip()

        products.append({
            "name": name,
            "price": price,
            "website": "Eldorado",
            "category": "Smartphone"
        })

    return products