from app.libs.download import DOWNLOAD
from flask import current_app


class YuShuBook:
    # isbn_url = 'https://api.douban.com/v2/book/isbn/{}'
    # keyword_url = 'https://api.douban.com/v2/book/search?q={}&count={}&start={}'
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    per_page = 15

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        res = DOWNLOAD.get(url)

        return res

    @classmethod
    def search_by_keyword(cls, keyword, page=1):

        url = cls.keyword_url.format(keyword,current_app.config['PER_PAGE'],cls.calaculed_start(page))
        res = DOWNLOAD.get(url)
        return res

    @staticmethod
    def calaculed_start(page):
        return (page-1)*current_app.config['PER_PAGE']