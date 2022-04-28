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