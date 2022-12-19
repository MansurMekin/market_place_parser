import json
import csv
import lxml
import requests
from bs4 import BeautifulSoup


def get_pages(category, page):
    lst = []
    for i in range(1, page + 1):
        url = f'https://www.sulpak.kz/f/{category}?page={i}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        laptop = [el.text for el in soup.find_all(
            'div', class_='product__item-name')]
        prices = [el.text for el in soup.find_all(
            'div', class_='product__item-price')]

        res = dict(zip(laptop, prices))

        for k, v in res.items():
            lst.append([k, v])
    return lst


categories = ['smartfoniy', 'smart_chasiy', 'naushniki', 'detskie_chasiy_s_gps',
              'smart_kolonki_umniye_kolonki', 'planshetiy', 'elektronniye_knigi',
              'stiralniye_mashiniy', 'sushilniye_apparatiy', 'piylesosiy', 'obogrevatelniye_priboriy', 
              'holodilniki', 'kuhonniye_kombajniy', 'myasorubki', 'led_oled_televizoriy', 'noutbuki', 
              'sistemniye_bloki', 'processoriy', 'igriy_dlya_pristavok', 'ukladka_volos']

for category in categories:
    data = get_pages(category, 15)
    with open(f'{category}.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'price'])
        writer.writerows(data)
        print(f'{category} готов')
