import requests
from bs4 import BeautifulSoup
link = "https://www.olx.ua/obyavlenie/2-kom-lukyanovka-dorogozhichi-ul-frunzekirillovskaya-124-IDFYLUw.html#198eafd9aa"
res = requests.get(link)

soup = BeautifulSoup(res.text, 'html.parser')
title = soup.find_all('h1')[0].text  # вызываем строку , которая заключена в теге h1 и выводим его в формате текст

title = title.replace('\n', '').replace('    ', '')
print(title)
# print(soup.find_all('h1'))
# print(title)

post_content = soup.find('div', {'class': 'clr lheight20 large'}).text
price = soup.find('strong', {'class': 'xxxx-large not-arranged'}).text


with open(f"flats/{title}.txt", 'w', encoding='utf-8') as file:
    file.write(post_content)
    file.write(f"\n{price}")
    file.write(f"\n{link}")
