from django.contrib import admin
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',blogHome,name='blogHhome'),
    path('<str:slug>',blogPost,name='blogPost')
]