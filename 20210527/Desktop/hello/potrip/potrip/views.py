# from datetime import datetime
from django.shortcuts import render


# def hello_world(request):
#     return render(request, 'hello_world.html', {
#         'current_time': str(datetime.now()),
#     })
from django.http import HttpResponse
from django import template
import os
# from potrip.models import Category

# def main(request):
#     return render(request, os.getcwd()+'\\potrip\\templates\\main.html', {'message':'hello'})

def main(request):
    with open(os.getcwd()+'\\potrip\\templates\\main.html', 'r') as reader:
        t = template.Template(reader.read())
    c = template.Context({'message':'hello'})
    return HttpResponse(t.render(c))
    # return HttpResponse(t.render(request, os.getcwd()+'\\potrip\\templates\\main.html', {'message':'hello'}))

def hello_world(request):
    return HttpResponse("Hello World!")

def math(request, a, b):
    a = float(a)
    b = float(b)
    s = a + b
    d = a - b
    p = a * b
    q = a / b
    with open(os.getcwd()+'\\potrip\\templates\\math.html', 'r') as reader:
    # with open('templates\\math.html', 'r') as reader:
        t = template.Template(reader.read())
    c = template.Context({'s': s, 'd': d, 'p': p, 'q': q})
    return HttpResponse(t.render(c))

# def showlist(request):
# 	return render(request, os.getcwd()+'\\potrip\\templates\\home.html')

def dropdownMenu(request):
    allCategory = Category.objects.all()
    return render(request, os.getcwd()+'\\potrip\\templates\\dropdownMenu.html', {'allCategory': allCategory})

    