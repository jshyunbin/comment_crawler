import datetime
import requests
from bs4 import BeautifulSoup as bs
from src.gmarket import gmarket
from review import Review


def market(flag):
    URL = flag.url
    MAX_COLLECT = flag.max_collect
    COLLECT_EMPTY = flag.collect_empty

    market = None
    soup = None

    if 'gmarket' in URL:
        print('using gmarket parser...')
        market = 'gmarket'
        merch_id = URL.split('?')[1].split('&')[0].split('=')[1]
        print(merch_id)
        ret = gmarket(merch_id, date_from=datetime.date(2020, 1, 1))
        print(ret)

    elif '11st' in URL:
        print('11st')
        market = '11st'
    elif 'shopping.naver' in URL:
        print('naver shopping')

        market = 'naver'
    elif 'coupang' in URL:
        print('coupang')

        page = requests.get(URL)
        soup = bs(page.text, "html.parser")

        market = 'coupang'

    if market is None:
        print('Cannot parse this url web site.')
        return


    if market == 'coupang':
        coupang_parse(soup)


def coupang_parse(soup):
    elements = soup.select('article.sdp-review__article__list')
    print('check')
    for index, e in enumerate(elements, 1):
        print(e)
