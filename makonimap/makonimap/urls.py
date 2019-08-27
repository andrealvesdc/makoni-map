"""makonimap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from makoni.views import search_adress
from makoni.views import index
from makoni.views import login
from makoni.views import create_account
from makoni.views import helper
from makoni.views import about
from makoni.views import contact
from makoni.views import error

"""
 -> Urls padrão;
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/',search_adress),
    path('login/',login),
    path('createuser',create_account),
    path('ajuda/',helper),
    path('sobre/',about),
    path('contato/',contact),
    path('error/', error),
    path('',index)
]
