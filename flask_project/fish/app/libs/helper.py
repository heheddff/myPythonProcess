# isbn13 13个0到9组成的数字
"""
    检测isbn
"""
def is_isbn_or_key(word):
    isbn_or_key = 'key'
    short_q = word.replace('-', '')

    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    if '-' in word and len(short_q) == 10 and short_q.isdigit():
        isbn_or_key = 'isbn'

    return isbn_or_key