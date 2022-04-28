import pymysql

import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

pymysql.version_info = (1, 4, 13, "final", 0)
pymysql.install_as_MySQLdb()

print(sys.getrecursionlimit())