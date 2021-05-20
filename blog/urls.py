from django.contrib import admin
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # API to post a comment
    path('postComment/',postComment, name='postComment'),

    # pages, we brought them down bcz slug is a string field and our post comment will not reach the desired url if we slug comes b4 it but we have added slashed to the end so it doesnt matter
    path('',blogHome,name='blogHome'),
    path('<str:slug>/',blogPost,name='blogPost'),

]