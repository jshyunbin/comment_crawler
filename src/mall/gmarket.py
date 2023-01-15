import datetime

from src.web.fetch import Fetch
from selectolax.parser import HTMLParser
from src.mall.review import Review, Reviews


class GMarket:
    @staticmethod
    def scrap(merch_id: str, date_from: datetime.date, opt):
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

        ret = Reviews(mall='gmarket', item=merch_id)

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
                    if not opt['collect_empty'] and k.css_first("p.con").text(strip=True) == '':
                        continue
                    review = Review(k.css_first("p.con").text(strip=True), date=date)
                    # print(review)
                    ret.append(review)
                if flag:
                    break

        return ret
