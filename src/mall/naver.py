import datetime
import json
from src.web.fetch import Fetch
from src.mall.review import Review

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Referer": ".shopping.naver.com",
}


class Naver:
    @staticmethod
    def scrap(merch_id: str, merch_no: str, date_from: datetime.date):
        res = Fetch.get(
            f"https://smartstore.naver.com/i/v1/reviews/paged-reviews?originProductNo={merch_id}&merchantNo={merch_no}&b",
            headers=headers
        )
        print(f"https://smartstore.naver.com/i/v1/reviews/paged-reviews?originProductNo=5993165160&merchantNo=511289869&b")
        print(res)
        root = json.loads(res)

        review_list = []
        for review_root in root['contents']:
            # review.merch_id = merch_id
            # review.fetch_date = datetime.datetime.now()
            date = review_root['createDate'].split("T")[0].split("-")
            date = [int(d) for d in date]
            date = datetime.date(*date)
            if date < date_from:
                break
            user = review_root['writerMemberId']
            review = Review(review_root['reviewContent'], date=date, user=user)
            review_list.append(review)
        return review_list


if __name__ == '__main__':
    li = Naver.scrap('5273934685', '500060220', datetime.date(2010, 1, 1))
    print(li[0])