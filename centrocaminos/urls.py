"""
URL configuration for centrocaminos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework.authtoken import views
from ccapp import views
from django.urls import re_path

urlpatterns = [
  path('',include('ccapp.urls')),
  path('admin/', admin.site.urls),
  re_path('signup', views.signup),
  re_path('login', views.login),
  re_path('test_token', views.test_token),
    path("__debug__/", include("debug_toolbar.urls")),
]


