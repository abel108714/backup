

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

def getLineFriendName(line_id):
    conn = pymysql.connect(**setDB())
    with conn.cursor() as cursor:
        sql="select name from line where line_id = "+str(line_id)
        print(sql)
        cursor.execute(sql)
        myresult = cursor.fetchall()
        conn.commit()
        cursor.close()
        if str(myresult) == str("()"):
            return 0
        else:
            return myresult  

def isLineFriendName(line_id):
    conn = pymysql.connect(**setDB())
    with conn.cursor() as cursor:
        sql="select name from line where line_id = '"+str(line_id)+"'"
        print(sql)
        cursor.execute(sql)
        myresult = cursor.fetchall()
        print(myresult)
        conn.commit()
        cursor.close()
        if str(myresult) == str("()"):
            return 0
        else:
            return True  

def insertLineFriendName(user_id,Name):
    print('===========================================')
    print("Name: " + str(Name))
    print("user_id: " + str(user_id))
    conn = pymysql.connect(**setDB())
    print("conn")
    with conn.cursor() as cursor:
        try:
            print("insert")
            sql="INSERT line (line_id,name) VALUES ('" + str(user_id) + "','" + str(Name)+"')"
            #sql="INSERT line (line_id,name) VALUES ('Uee6224531167e863e3c08504055d6ed2','周立修')"
            print(sql)
            cursor.execute(sql)
            #return 0
        except Exception as e:
            print(e)
            #print("UPDATE")
            #sql="UPDATE line SET name="+str(Name)+" where line_id="+str(user_id)
            #print(sql)
            #cursor.execute(sql)          

        conn.commit()
        cursor.close()

def ppp(user_id,Name):
    print('Name: ' + str(Name))
    print('user_id: ' + str(user_id))

def getPermission(user_id):
    print("checkPermission")
    conn = pymysql.connect(**setDB())
    print("conn")
    print('user_id: ' + str(user_id))
    with conn.cursor() as cursor:
        try:
            print("insert")
            sql="select permission_name from line where line_id = '" + str(user_id) + "'"
            print(sql)
            #sql="select * from line_permission where = " + str(permission_name)

            cursor.execute(sql)
            # myresult = cursor.fetchall()
            # for myresultArr in myresult:
            #     print(myresultArr[0])
            # print("myresult = " + str(myresult))       
            myresult = cursor.fetchone()
            print("myresult = " + str(myresult))   
            print("myresult[0] = " + str(myresult[0]))   
            if str(myresult[0]) == "None":
                print("NULL")   
                return "NULL"
            else:
                print(myresult[0])
                getPermissionArr(myresult[0])
                return myresult[0]
            #sql="INSERT line (line_id,name) VALUES ('" + str(user_id) + "','" + str(Name)+"')"
            #sql="INSERT line (line_id,name) VALUES ('Uee6224531167e863e3c08504055d6ed2','周立修')"

            #return 0
        except Exception as e:
            print("UPDATE")
            #sql="UPDATE line SET name="+str(Name)+" where line_id="+str(user_id)
            #print(sql)
            #cursor.execute(sql)          

        conn.commit()
        cursor.close()


def getPermissionArr(permission_name):
    print("checkPermission")
    conn = pymysql.connect(**setDB())
    print("conn")
    print('permission_name: ' + str(permission_name))
    with conn.cursor() as cursor:
        try:
            print("select")
            sql="select `order`, dsv_inv, finished_product_inv, pp, prom from line_permission where permission_name = '" + str(permission_name) + "'"
            print(sql)
            #sql="select * from line_permission where = " + str(permission_name)

            cursor.execute(sql)
            myresult = cursor.fetchall()
            for myresultArr in myresult:
                print(myresultArr)
            print("myresult = " + str(myresult))      
            print("1") 
            myresult = cursor.fetchone()
            print("2")
            print("myresult = " + str(myresult))   
            print("myresult[0] = " + str(myresult[0]))   
            if str(myresult[0]) == "None":
                print("NULL")   
                return "NULL"
            else:
                print(myresult[0])   
                return myresult[0]
            #sql="INSERT line (line_id,name) VALUES ('" + str(user_id) + "','" + str(Name)+"')"
            #sql="INSERT line (line_id,name) VALUES ('Uee6224531167e863e3c08504055d6ed2','周立修')"

            #return 0
        except Exception as e:
            print("UPDATE")
            #sql="UPDATE line SET name="+str(Name)+" where line_id="+str(user_id)
            #print(sql)
            #cursor.execute(sql)          

        conn.commit()
        cursor.close()


if __name__ == "__main__":
    print("start")



    getPermission("Uee6224531167e863e3c08504055d6ed2")
