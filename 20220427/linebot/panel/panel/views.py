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