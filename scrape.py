import requests as req
from bs4 import BeautifulSoup as soup

def get_data():
    BASE_URL = 'https://www.moneycontrol.com/stocks/marketstats/blockdeals/'
    print("[Request Sent]")
    request = req.get(BASE_URL)
    print(f"[TIME ELAPSED]: {request.elapsed}")
    soup_object = soup(request.text, 'html.parser')

    scripts = {}

    for endpoint in soup_object.find_all('td', class_='PR'):
        company = endpoint.span.a.text
        if company not in scripts.keys():
            scripts[company] = 1
            continue
        scripts[company] += 1

    return scripts