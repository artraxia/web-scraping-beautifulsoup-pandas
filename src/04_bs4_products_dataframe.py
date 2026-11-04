"""Exercícios 7.4 a 7.6 — BeautifulSoup: nomes e preços dos produtos em um DataFrame.

Lição do 7.4: os nomes estão em tags <p> (não <div>), identificadas pela classe.
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = "https://tripleten-com.github.io/simple-shop_pt-br/"
soup = BeautifulSoup(requests.get(URL).text, "lxml")

# 7.4 — nomes
name_products = [
    row.text
    for row in soup.find_all("p", attrs={"class": "t754__title t-name t-name_md js-product-name"})
]

# 7.5 — preços
price = [
    row.text
    for row in soup.find_all("p", attrs={"class": "t754__price-value js-product-price"})
]

# 7.6 — DataFrame
products_data = pd.DataFrame({"name": name_products, "price": price})
print(products_data.head())
