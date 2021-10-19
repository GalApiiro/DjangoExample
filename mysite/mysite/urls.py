"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from Animals import dog
import re
import book_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dogs/list/', dog.Dog.list_dogs),
    path('unknownhandler/', re.compile), # an example for a view method that cannot be resolved
    path('delete_book/', book_views.delete_book),
    path('get_books/', book_views.Library.get_books)
]
