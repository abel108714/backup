import pymysql

import sys
sys.setrecursionlimit(3500)
#print(sys.getrecursionlimit())

pymysql.version_info = (1, 4, 13, "final", 0)
pymysql.install_as_MySQLdb()



from django.db import connection
cursor = connection.cursor()

