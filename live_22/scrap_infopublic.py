"""
Script que verifica o site da infopublic e baixa todos os brasões para um diretório no computador.
"""



from bs4 import BeautifulSoup as bs
from requests import get
import os

base_url = 'http://infopublic.com.br/'

info = get(base_url)
info_page = bs(info.text, 'html.parser')

boxes = info_page.find_all('img', {'alt': 'Brasão de cidade'})

src = []
for box in boxes:
    sources = box.attrs['src']
    src.append(sources)

url_images = []

for s in src:
    url_images.append(f'{base_url}{s}')

os.makedirs('brasoes', exist_ok=True)

for url in url_images:
    print('Downloading image %s...' % (url))
    res = get(url)

    with open(os.path.join('brasoes', os.path.basename(url)), 'wb') as imageFile:
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)


print('Done!')