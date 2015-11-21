#coding=utf-8
import sqlite3

class SqliteWrapper:
    def __init__(self):
        self.__conn = None
        self.__cursor = None

    def __del__(self):
        self.close()

    def connect(self, dbfile):
        self.close()
        self.__conn = sqlite3.connect(dbfile)
        self.__cursor = self.__conn.cursor()

    def close(self):
        if self.__cursor:
            self.__cursor.close()
            self.__cursor = None

        if self.__conn:
            self.__conn.close()
            self.__conn = None

    def select(self, sql):
        self.__cursor.execute(sql)
        return self.__cursor.fetchall()

    def execute(self, sql):
        try:
            self.__cursor.execute(sql)
            self.__conn.commit()
        except Exception as e:
            print(e)


    def execute_batch(self, sqls):
        for sql in sqls:
            self.__cursor.execute(sql)
        self.__conn.commit()
