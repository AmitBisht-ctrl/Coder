from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
# from django.http import HttpResponse

# Create your views here.
def blogHome(request):
    return render(request,'blog/blogHome.html')

def blogPost(request,slug):
    return render(request,'blog/blogPost.html')