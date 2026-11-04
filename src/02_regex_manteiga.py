"""Exercício 7.2 — nomes de produtos contendo "Manteiga", sem o peso.

Erro comum: o padrão 'Manteiga*' significa "Manteig" seguido de zero ou mais 'a',
e não "qualquer coisa com Manteiga". O lookahead (?=,) para antes da vírgula.
"""

import re

import requests

URL = "https://tripleten-com.github.io/simple-shop_pt-br/"
req_text = requests.get(URL).text

print(re.findall(".*?Manteiga.*?(?=,)", req_text))
