import pymysql

import sys


try:
    #sys.setrecursionlimit(2000)
    # print(sys.getrecursionlimit())
    # sys.setrecursionlimit(10000000000)
    # print(sys.getrecursionlimit())

    #pymysql.version_info = (1, 4, 13, "final", 0)
    pymysql.install_as_MySQLdb()

except Exception as e:
    print(e)


# import pymysql
# pymysql.version_info = (1, 4, 0, "final", 0)
# pymysql.install_as_MySQLdb()





