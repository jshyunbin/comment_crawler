import datetime
from mall import *


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
        ret = gmarket(merch_id, datetime.date(2020, 1, 1), opt)

    elif '11st' in URL:
        print('11st')
        mall = '11st'
    elif 'shopping.naver' in URL:
        print('naver shopping')

        mall = 'naver'
    elif 'coupang' in URL:
        print('coupang')


        mall = 'coupang'

    if mall is None:
        print('Cannot parse this url web site.')
        return


    if mall == 'coupang':
        coupang_parse(soup)


def coupang_parse(soup):
    pass