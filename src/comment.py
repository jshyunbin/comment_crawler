

class Comment:
    def __init__(self, context, title='', date=None, user=None, star='', rcmd=''):
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

