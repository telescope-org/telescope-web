from flask import app
import pymysql

from common.logger import Logger


class MySQLConnection(object):

    def __init__(self) -> None:
        self.db = pymysql.connect(host='',
                               port=0,
                               user='',
                               passwd='',
                               charset='utf8'
                               )
        self.cursor = self.db.cursor()

    def check(self):
        self.cursor.execute("SELECT VERSION()")
        data = self.cursor.fetchone()
        print (f"Database version : {data} ")


    def exec_sql(self, sql):
        try:
            res_val = self.cursor.execute(sql)
            self.db.commit()
            return res_val
        except Exception as e:
            Logger.error(f'error message: {e}!')
            self.db.rollback()
            return -1

    def select_all(self, sql):
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            Logger.error(f"Error: unable to fetch data, error message: {e}!")
            print("Error: unable to fetch data")

