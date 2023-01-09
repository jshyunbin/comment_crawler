import datetime
import requests
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

        url_data = URL.split('?')[1].split('&')
        merch_id = ""
        for data in url_data:
            if 'goodscode' in data.lower():
                merch_id = data.split('=')[1]
        
        if merch_id == '':
            print('invalid url')
            return

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


        market = 'coupang'

    if market is None:
        print('Cannot parse this url web site.')
        return


    if market == 'coupang':
        coupang_parse(soup)


def coupang_parse(soup):
    pass