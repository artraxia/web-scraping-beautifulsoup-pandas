# Web Scraping with Python — Regex, BeautifulSoup & pandas

![Python](https://img.shields.io/badge/python-3.10%2B-blue) ![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4-green) ![License: MIT](https://img.shields.io/badge/license-MIT-green)

Exercícios de extração de dados da página de exemplo
[simple-shop_pt-br](https://tripleten-com.github.io/simple-shop_pt-br/), do programa **Data Scientist** da TripleTen.

## Conteúdo

| Script | Exercício | Técnica |
|---|---|---|
| `src/01_regex_title.py` | 7.1 — tag `<title>` | `re.search`, quantificador não-guloso `.*?` |
| `src/02_regex_manteiga.py` | 7.2 — produtos com "Manteiga" | `re.findall`, lookahead `(?=,)` |
| `src/03_regex_horizon.py` | 7.3 — produtos da marca "Horizon" | classes de caracteres `[A-Za-z0-9\s\-%]` |
| `src/04_bs4_products_dataframe.py` | 7.4 a 7.6 — nomes, preços e DataFrame | `BeautifulSoup.find_all` por classe, `pandas.DataFrame` |

## Key findings

- A página tem 30 produtos; o scraping com BeautifulSoup recupera todos com nome e preço em um DataFrame de 30 × 2.
- Regex resolve capturas pontuais (`<title>`, uma marca), mas é frágil para estrutura HTML; para dados tabulares o parser é mais confiável e legível.

## Como executar

```bash
pip install -r requirements.txt
python src/04_bs4_products_dataframe.py
```

## Aprendizados

- Regex é frágil para HTML; serve para capturas pontuais (`<title>`, um padrão de texto). Para estrutura, BeautifulSoup.
- `'Manteiga*'` não significa "qualquer coisa com Manteiga" — o `*` se aplica só ao último caractere.
- Inspecionar o HTML antes de escrever o seletor: o gabarito pedia `<p>`, não `<div>`.
