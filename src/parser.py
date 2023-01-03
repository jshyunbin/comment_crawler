import requests
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from comment import Comment


def parser(flag):
    URL = flag.url
    MAX_COLLECT = flag.max_collect
    COLLECT_EMPTY = flag.collect_empty
    BROWSER = flag.browser

    market = None
    soup = None

    if 'gmarket' in URL:
        print('using gmarket parser...')
        market = 'gmarket'

        if BROWSER == 'Safari':
            browser = webdriver.Safari()
        else:
            browser = webdriver.Firefox()

        try:
            browser.get(URL)
            browser.find_element(value='txtReviewTotalCount').click()
            time.sleep(0.5)

            soup = bs(browser.page_source, 'html.parser')
        except Exception as e:
            print(e)

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
    elif market == 'gmarket':
        gmarket_parse(soup)


def coupang_parse(soup):
    elements = soup.select('article.sdp-review__article__list')
    print('check')
    for index, e in enumerate(elements, 1):
        print(e)


def gmarket_parse(soup):
    prem_comments = []
    norm_comments = []

    elements = soup.select('div#premium-wrapper table tr')

    for element in elements:
        title = element.select_one('p.comment-tit').text
        context = element.select_one('p.con').text
        writer = element.select('dl.writer-info dd')
        user = writer[0].text
        date = writer[1].text
        hit = writer[2].text
        prem_comments.append(Comment(context, title, date, user, rcmd=hit))

    elements = soup.select('div#text-wrapper table tr')

    for element in elements:
        context = element.select_one('p.con').text
        writer = element.select('dl.writer-info dd')
        user = writer[0].text
        date = writer[1].text
        norm_comments.append(Comment(context, user=user, date=date))

    for comment in prem_comments:
        print(comment)

    for comment in norm_comments:
        print(comment)
