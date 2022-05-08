import pymysql
pymysql.version_info = (1, 4, 13, "final", 0)
#解決版本問題，django.core.exceptions.ImproperlyConfigured: mysqlclient 1.4.0 or newer is required; you have 0.10.1.
pymysql.install_as_MySQLdb()