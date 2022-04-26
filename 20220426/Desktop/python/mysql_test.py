import pymysql
#import charts
# 資料庫設定
db_settings = {
    "host": "127.21.7.39",
    "port": 3306,
    "user": "root",
    "password": "16264386",
    "db": "usersDB",
    "charset": "utf8"
}


# 建立Connection物件
conn = pymysql.connect(**db_settings)
# 建立Cursor物件
with conn.cursor() as cursor:
    sql="INSERT INTO users(UID,Dept,Name,checked) VALUES(%s,%s,%s,%s)"
    data=(6,'網通','周立修','S')
    cursor.execute(sql,data)
    # 儲存變更
    conn.commit()

#INSERT INTO users(ID,Dept,Name,checked) VALUES('1','2','3','4')