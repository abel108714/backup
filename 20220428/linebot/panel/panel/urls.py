"""panel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


# from django.contrib import admin
# from django.http import request
# from django.urls import path, re_path
# #from panel.views import hello_world, math
# from panel.views import math

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     #path('hello/', hello_world),
#     re_path(r'(\d{1,2})/math/(\d{1,2})/', math),
# ]


from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('panel/', include('panel.urls')),
    path('admin/', admin.site.urls),
]