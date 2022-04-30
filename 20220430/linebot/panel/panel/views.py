from django.http import HttpResponse
from django import template
import os
def math(request, a, b):
    a = float(a)
    b = float(b)
    s = a + b
    d = a - b
    p = a * b
    q = a / b
    with open(os.getcwd()+'\\panel\\templates\\math.html', 'r') as reader:
        t = template.Template(reader.read())
    c = template.Context({'s': s, 'd': d, 'p': p, 'q': q})
    return HttpResponse(t.render(c))


# 需要導入模塊: from blog import models [as 別名]
# 或者: from blog.models import Article [as 別名]
# import datetime
# from github3 import authorize
# from blog import models
# from blog.models import Article
 
# def show(request, article_id):
#     article = Article.objects.get(pk=article_id)
#     authorize(request.user, 'read', article)
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html) 


from django.http import HttpResponse

def index(request):
    return HttpResponse("这里是liujiangblog.com的投票站点")



from django.db import connection
def getdata():
    
    with connection.cursor() as cursor:
        cursor.execute("select * from line limit 1")
        rtn_data = cursor.fetchall()
    return rtn_data

def getWorkChartsByPercent():
    cursor = connection.cursor()
    sql = "select sum(notes->'$.insert') `insert`,sum(notes->'$.delete') `delete`,sum(notes->'$.update') `update`," \
          "sum(notes->'$.create') `create`,sum(notes->'$.alter') `alter` from %s" % TABLE
    cursor.execute(sql)
    field_names = [item[0] for item in cursor.description]
    rawData = cursor.fetchall()
    #
    result = []
    for row in rawData:
        objDict = {}
        # ?????????????Dict?
        for index, value in enumerate(row):
            objDict[field_names[index]] = value
        result.append(objDict)
    return result

def getWorkChartsByPercent():
    cursor = connection.cursor()
    sql = "select * from line limit 1"
    cursor.execute(sql)
    field_names = [item[0] for item in cursor.description]
    rawData = cursor.fetchall()
    #
    result = []
    for row in rawData:
        objDict = {}
        # ?????????????Dict?
        for index, value in enumerate(row):
            objDict[field_names[index]] = value
        result.append(objDict)
    return result
# cursor = connection.cursor()
# def insertPromData(id,product_name,special_offer,special_purchase_price,note):
#     conn = pymysql.connect(**setDB())
    
#     # 建立Cursor物件
#     with conn.cursor() as cursor:

#         print("insertPromData123")
#         try:
#             print("insertPromData456")


#             cursor.execute(sql)#,data)
#         except Exception as e:
#             print(e)
#             print("錯誤")
#             sql2 = "DELETE FROM prom where id"+str(id)
#             cursor.execute(sql2)
#             cursor.execute(sql)
#         # 儲存變更
#         conn.commit()