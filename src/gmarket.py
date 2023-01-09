import datetime

from fetch import Fetch
from selectolax.parser import HTMLParser
from review import Review


def gmarket(merch_id: str, date_from: datetime.date):
    res = Fetch.post(
        "http://item.gmarket.co.kr/Review", data={"goodsCode": merch_id}
    )
    root = HTMLParser(res)
    link = [
        "http://item.gmarket.co.kr/Review/Premium",
        "http://item.gmarket.co.kr/Review/Text",
    ]
    review_count = list(
        map(lambda x: int(x.text()), root.css("span.pagetotal > em"))
    )

    ret = []

    for j in range(2):
        for i in range(review_count[j]):
            res = Fetch.post(
                link[j],
                data={
                    "goodsCode": merch_id,
                    "pageNo": i + 1,
                    "totalPage": review_count[j],
                    "sort": 1,
                },
            )
            root = HTMLParser(res)
            flag = False
            for k in root.css("tbody > tr"):
                date = list(
                    map(
                        int,
                        k.css_first("dl.writer-info > dd:nth-child(4)")
                        .text()
                        .split("."),
                    )
                )
                date = datetime.datetime(*date)
                if date.date() < date_from:
                    flag = True
                    break
                review = Review(k.css_first("p.con").text(strip=True), date=date)
                # print(review)
                ret.append(review)
            if flag:
                break

    return ret