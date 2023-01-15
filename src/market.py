import datetime
from mall import *
from src.web.fetch import Fetch
from selectolax.parser import HTMLParser
import json


def market(flag):
    URL = flag.url

    opt = {
        'collect_empty': flag.collect_empty,
        'max_collect': flag.max_collect
            }

    mall = None
    soup = None

    if 'gmarket' in URL:
        print('using gmarket parser...')
        mall = 'gmarket'

        url_data = URL.split('?')[1].split('&')
        merch_id = ""
        for data in url_data:
            if 'goodscode' in data.lower():
                merch_id = data.split('=')[1]
        
        if merch_id == '':
            print('invalid url')
            return

        print(merch_id)
        ret = gmarket.GMarket.scrap(merch_id, datetime.date(2020, 1, 1), opt)

    elif '11st' in URL:
        print('11st')
        mall = '11st'
    elif 'naver' in URL:
        print('using naver shopping parser...')

        ret = Fetch.get(URL)
        root = HTMLParser(ret)
        print(ret)
        info = root.css_first("body > script").text()
        # print(info[:50])
        info = json.loads(info.split('_=')[1])
        info = info['product']['A']
        productNo = info['productNo']
        merchNo = info['channel']['naverPaySellerNo']

        ret = naver.Naver.scrap(productNo, merchNo, datetime.date(2010, 1, 1))
        [print(ret[i]) for i in range(5)]

        mall = 'naver'
    elif 'coupang' in URL:
        print('coupang')


        mall = 'coupang'

    if mall is None:
        print('Cannot parse this url web site.')
        return

