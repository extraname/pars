import requests
from bs4 import BeautifulSoup


def find_flats():
    result = requests.get('https://www.olx.ua/nedvizhimost/kvartiry-komnaty/arenda-kvartir-komnat/kiev/#from404')
    soup = BeautifulSoup(result.text, 'html.parser')

    necessary_block = soup.find('div', {'class': 'rel listHandler'})
    # print(necessary_block)
    for a in necessary_block.find_all('tr', {'class': 'offer-wrapper'}):
        yield a['href']


def list_flat(url: str):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.find_all('h1')[0].text

    title = title.replace('\n', '').replace('    ', '')
    post_content = soup.find('div', {'class': 'clr lheight20 large'}).text
    price = soup.find('strong', {'class': 'xxxx-large not-arranged'}).text

    with open(f"flats/{title}.txt", 'w', encoding='utf-8') as file:
        file.write(post_content)
        file.write(f"\n{price}")
        file.write(f"\n{url}")


if __name__ == "__main__":
    for link in find_flats():
        list_flat(link)
