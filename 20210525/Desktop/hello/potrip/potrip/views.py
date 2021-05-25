# from datetime import datetime
# from django.shortcuts import render


# def hello_world(request):
#     return render(request, 'hello_world.html', {
#         'current_time': str(datetime.now()),
#     })
from django.http import HttpResponse
from django import template
import os

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
        t = template.Template(reader.read())
    c = template.Context({'s': s, 'd': d, 'p': p, 'q': q})
    return HttpResponse(t.render(c))

    