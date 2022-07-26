import datetime
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def collect_data(city_code="25257"):
    cur_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_$M')
    ua = UserAgent()

    headers = {
        'accept': 'text / html, application / xhtml + xml, application / xml; q = 0.9, image / avif, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange; v = b3; q = 0.9',
        'User-Agent': ua.random
    }

    response = requests.get(url='https://www.shatura.com/sitemap_goods.xml', headers=headers)

    with open(f'sitemap.html', 'w', encoding='utf8') as file:
        file.write(response.text)

    #with open('sitemap_goods.html') as file:
    #    src = file.read()

    #soup = BeautifulSoup(src, 'lxml')

def main():
    collect_data(city_code='25257')

if __name__ == '__main__':
    main()