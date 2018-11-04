"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from register.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('listype/', Listype, name="Listype"),
    path('newtype/', Newtype, name="Newtype"),
    path('uptype/<int:id>/', Uptype, name="Uptype"),
    path('deltype/<int:id>/', Deltype, name="Deltype"),
    path('lisprod/', LisProd, name="LisProduct"),
    path('newprod/', NewProd, name="NewProduct"),
    path('upprod/<int:id>/', UpProd, name="UpProduct"),
    path('delprod/<int:id>/', DelProd, name="DelProduct"),
    path('liscli/', LisCli, name="LisClient"),
    path('newcli/', NewCli,  name="NewClient"),
    path('upcli/<int:id>/', UpCli, name="UpClient"),
    path('delcli/<int:id>/', DelCli, name="DelClient"),
]
