"""Exercício 7.1 — capturar a tag <title> da página com re.search."""

import re

import requests

URL = "https://tripleten-com.github.io/simple-shop_pt-br/"
req_text = requests.get(URL).text

# .*? é não-guloso: para no primeiro </title> encontrado
print(re.search("<title>.*?</title>", req_text).group())
