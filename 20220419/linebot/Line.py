


def setDB():
    # 資料庫設定
    db_settings = {
        "host": "127.21.7.39",
        "port": 3306,
        "user": "root",
        "password": "16264386",
        "db": "invdb",
        "charset": "utf8"
    }
    return db_settings

# def getLineFriendName(line_id):
#     conn = pymysql.connect(**setDB())
#     with conn.cursor() as cursor:
#         sql="select name from line where line_id = "+str(line_id)
#         print(sql)
#         cursor.execute(sql)
#         myresult = cursor.fetchall()
#         conn.commit()
#         cursor.close()
#         if str(myresult) == str("()"):
#             return 0
#         else:
#             return myresult  

# def insertLineFriendName(line_id,name):
#     print("Name : " + str(Name))
#     print("user_id : " + str(user_id))
#     conn = pymysql.connect(**setDB())
#     with conn.cursor() as cursor:
#         try:
#             sql="INSERT line (line_id,name) VALUES ("+str(line_id)+","+str(name)+")"
#             print(sql)
#             cursor.execute(sql)
#             return 0
#         except Exception as e:
#             sql="UPDATE line SET name="+str(name)+" where line_id="+str(line_id)
#             print(sql)
#             cursor.execute(sql)          
#             return 1




