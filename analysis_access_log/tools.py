import pandas
import sqlite3
import os


class SavePandas(object):

    def __init__(self, filename, contents):
        self.filename = filename
        # self.contents = contents
        self.ps = pandas.DataFrame(contents)

    def save_to_excel(self):
        if self.check_file("{}.xlsx".format(self.filename)) is False:
            try:
                self.ps.to_excel("{}.xlsx".format(self.filename), encoding='utf8')
            except Exception as e:
                print(e)

    def save_to_sqlite(self, append=False):
        try:
            with sqlite3.connect('data.sqlite') as db:
                if append:
                    self.ps.to_sql(self.filename, con=db, if_exists='append')
                else:
                    self.ps.to_sql(self.filename, con=db)
        except Exception as e:
            print(e)

    @staticmethod
    def check_file(file):
        if os.path.isfile(file) is False:
            print("{} is not exists".format(file))
            return False
        else:
            return True

    @staticmethod
    def sort_by_num(res):
        try:
            new_items = list(res.items())
            new_items.sort(key=lambda x: x[1], reverse=True)
        except Exception as e:
            print(e)
            return []
        else:
            return new_items
