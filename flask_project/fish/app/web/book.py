from flask import jsonify,request,render_template,flash
from app.web.webblue import web
from app.forms.book import SearchForm

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook


@web.route('/book/search')
def search():
    # isbn_url = 'https://api.douban.com/v2/book/isbn/{}'
    # keyword_url = 'https://api.douban.com/v2/book/search?q={}&count={}&start={}'
    # isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    # keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            res = YuShuBook.search_by_isbn(q)
        else:
            res = YuShuBook.search_by_keyword(q)

        return jsonify(res)
    else:
        return jsonify(form.errors)

@web.route('/test')
def test():
    data = {
        'name': '',
        'age': 18
    }
    flash('message flash', category='error')
    flash('message flash TWO')
    return render_template('book/test.html', data=data)
