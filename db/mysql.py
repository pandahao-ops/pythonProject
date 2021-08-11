import pymysql


class HighPipMysql:
    def __init__(self):
        self.mysql = pymysql.connect(host="192.168.100.3",
                                     user="root",
                                     password="123456",
                                     port=3306,  # 端口
                                     database="python",
                                     charset='utf8')

    def test(self):
        cursor = self.mysql.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        print("Database version : %s " % data)


if __name__ == '__main__':
    t = HighPipMysql()
    t.test()
