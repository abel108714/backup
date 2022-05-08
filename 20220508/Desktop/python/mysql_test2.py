
#import charts
# 資料庫設定
import mysql.connector

mydb=mysql.connector.connect(
    host= '127.21.7.39',
    port= 3306,
    user= 'root',
    password= '16264386',
    db= 'usersDB'
)

cur=mydb.cursor()
sql="INSERT INTO users(UID,Dept,Name,checked) VALUES(%s,%s,%s,%s)"
my_id=123#str(event.source.user_id)
data=(my_id,'',str("周立修"),'')
cur.execute(sql,data)
mydb.commit()




#INSERT INTO users(ID,Dept,Name,checked) VALUES('1','2','3','4')