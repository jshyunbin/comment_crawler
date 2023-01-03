# 🐛 Comment Crawler

This web crawler targets korean online shopping mall comments. 

```zsh
python src/main.py -url "http://item.gmarket.co.kr/Item?goodscode=2405613985&ver=638083484789237196
```

## Supporting Websites

- [G마켓](http://www.gmarket.co.kr)
- [11번가](https://www.11st.co.kr) (wip)
- [Naver shopping](https://shopping.naver.com/home) (wip)
- [coupang](https://www.coupang.com) (wip)

## How to use

Comment crawler uses flags to specify 

| Flags         | type    | description                                                      | default  |
|---------------|---------|------------------------------------------------------------------|----------|
| url           | string  | URL link of the online shopping website.                         | None     |
| max_collect   | int     | Maximum number of comments to collect. -1 if no limit.           | -1       |
| collect_empty | boolean | Collects empty comments if set to True                           | True     |
| browser       | enum    | Browser used for selenium. Can choose between Safari and Firefox | 'Safari' |
