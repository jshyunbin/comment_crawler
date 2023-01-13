from src.web.fetch import Fetch



class Coupang:
    URL = "https://www.coupang.com"

    _REQUEST_HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    }
    _COOKIES = {
        # Update PCID when coupang is not working. PCID can be found in the network tab of the browser console.
        "PCID": "10790271030004111726842",
    }

    @classmethod
    def get_comment(cls, opt):
        link = '/vp/product/reviews'

        res = Fetch.post(Coupang.URL + link, data={
            'productId': '5647481827',
            'page': 1,
            'size': 5,
            'sortBy': 'DATE_DESC',
            'ratings': 'null',
            'q': '',
            'viRoleCode': 0,
            'ratingSummary': 'true'
        }, skip_auto_headers=Coupang._REQUEST_HEADERS, cookies=Coupang._COOKIES)
        print(res)



if __name__ == "__main__":
    Coupang.get_comment({})
