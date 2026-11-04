"""Exercício 7.3 — produtos da marca "Horizon".

Requisito: "Horizon" no início, seguido de letras, dígitos, espaços, hifens e '%',
parando antes da vírgula.
"""

import re

import requests

URL = "https://tripleten-com.github.io/simple-shop_pt-br/"
req_text = requests.get(URL).text

pattern = r"Horizon[A-Za-z0-9\s\-%]+(?=,)"
found_products = re.findall(pattern, req_text)

print(len(found_products))
print(found_products)
