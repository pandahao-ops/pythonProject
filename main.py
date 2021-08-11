# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from db import redis
from db import mysql
from config import req

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    r = redis.HighPipRedis()
    r.set_v_ttl("bar", "foo", 11)
    print(r.ttl("bar"))

    m = mysql.HighPipMysql()
    m.test()

    c = req.get("https://www.baidu.com")
    print(c.status_code)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
