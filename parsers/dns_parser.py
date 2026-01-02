import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.dns-shop.ru/catalog/17a8a01d16404e77/smartfony/"

def parse_dns():
    products = []
    headers = {"User-Agent": "Mozilla/5.0"}

    for page in range(1, 6):
        url = f"{BASE_URL}?p={page}"
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")

        items = soup.select("div.catalog-product")
        for item in items:
            name = item.select_one(".catalog-product__name").text.strip()
            price = item.select_one(".product-buy__price").text.strip()

            products.append({
                "name": name,
                "price": price,
                "website": "DNS",
                "category": "Smartphone"
            })

    return products