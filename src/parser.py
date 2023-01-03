import requests
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from comment import Comment


def parser(url, max_collect, collect_empty):
    market = None
    if 'gmarket' in url:
        print('gmarket')
        market = 'gmarket'
    elif '11st' in url:
        print('11st')
        market = '11st'
    elif 'shopping.naver' in url:
        print('naver shopping')
        market = 'naver'
    elif 'coupang' in url:
        print('coupang')
        market = 'coupang'

    if market is None:
        print('Cannot parse this url web site.')
        return

    page = requests.get(url)
    soup = bs(page.text, "html.parser")

    if market == 'coupang':
        coupang_parse(soup)
    elif market == 'gmarket':
        gmarket_parse(url)


def coupang_parse(soup):
    elements = soup.select('article.sdp-review__article__list')
    print('check')
    for index, e in enumerate(elements, 1):
        print(e)


def gmarket_parse(url):
    browser = webdriver.Safari()
    soup = None
    prem_comments = []
    norm_comments = []

    try:
        browser.get(url)
        browser.find_element(value='txtReviewTotalCount').click()
        time.sleep(0.5)

        soup = bs(browser.page_source, 'html.parser')
    except Exception as e:
        print(e)

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
