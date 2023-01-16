import datetime
import json

import selectolax.parser

from src.web.fetch import Fetch
from src.mall.review import Review, Reviews


class Naver:
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "Referer": ".shopping.naver.com",
    }

    @classmethod
    def scrap(cls, merch_id: str, merch_no: str, date_from: datetime.date):
        link = "https://smartstore.naver.com/i/v1/reviews/paged-reviews"
        pg = 1

        review_list = Reviews(mall='naver', item=merch_id)
        while True:
            res = Fetch.post(
                link,
                data={
                    'page': pg,
                    'pageSize': 20,
                    'sortType': 'REVIEW_CREATE_DATEDESC',
                    'originProductNo': f'{merch_id}',
                    'merchantNo': f'{merch_no}'
                },
                headers=cls.HEADERS
            )
            if selectolax.parser.HTMLParser(res).text() == 'OK':
                break
            root = json.loads(res)


            for review_root in root['contents']:
                date = review_root['createDate'].split("T")[0].split("-")
                date = [int(d) for d in date]
                date = datetime.date(*date)
                if date < date_from:
                    return review_list
                user = review_root['writerMemberId']
                score = review_root['reviewScore']
                review = Review(review_root['reviewContent'], date=date.__str__(), user=user, star=score)
                review_list.append(review)
        return review_list


if __name__ == '__main__':
    li = Naver.scrap('5273934685', '500060220', datetime.date(2010, 1, 1))
    print(len(li))
