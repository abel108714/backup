

import pymysql

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



def isProductExist(product_id):
    conn = pymysql.connect(**setDB())
    with conn.cursor() as cursor:
        print("1")
        try:
            print("2")
            sql="select count(product_id) from product where product_id = '"+str(product_id)+"'"#顯示資料
            print("sql : "+str(sql))
            cursor.execute(sql)
            myresult = cursor.fetchone()
            # print(myresult)
            conn.commit()
            cursor.close()
            print(myresult[0])
            # print(myresult[1])

            
        except Exception as e:
            print("3")
            print(e)
            # return False
        print("4")
        if myresult[0] == 0:
            return False
        else:
            return True
        # return False

def insertProduct(product_id,product_name):#輸入品號品名
    # sql="insert product(product_id,product_name) values('"+str(product_id)+"','"+str(product_name)+"')"
    conn = pymysql.connect(**setDB())
    # 建立Cursor物件
    if isProductExist(product_id) == True:
        with conn.cursor() as cursor:
            try:
                sql="insert product(product_id,product_name) values('"+str(product_id)+"','"+str(product_name)+"')"
                print("insertProduct")
                print("sql : "+str(sql))
                cursor.execute(sql)
            except Exception as e:
                print(e)
            # 儲存變更
            conn.commit()



print(isProductExist('10903004'))

