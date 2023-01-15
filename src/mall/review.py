import json
from datetime import datetime


class Reviews:
    def __init__(self, mall: str, item: str):
        self.ls = []
        self.mall = mall
        self.item = item

    def append(self, r):
        self.ls.append(r)

    def extend(self, rs):
        self.ls.extend(rs.ls)


    def write_json(self, filename: str, opt):
        with open(filename, 'x') as f:
            f.write(f'{{"scrap_time": "{datetime.now()}", "mall": "{self.mall}", "item": "{self.item}", '
                    f'"reviews": [{", ".join([json.dumps(r) for r in self.ls])}]}}')

    def __len__(self):
        return len(self.ls)


class Review:
    def __init__(self, context, title='', date=None, user='', star='', rcmd=''):
        self.title = title.strip()
        self.context = context.strip()
        self.date = date
        self.user = user
        self.star = star
        self.rcmd = rcmd

    def __str__(self):
        if self.title == '':
            return 'comment by user ' + self.user + ': ' + self.context
        else:
            return 'comment by user ' + self.user + ': ' + self.title

    def is_empty(self):
        return self.context is None or self.context == ""



