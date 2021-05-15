from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
# from django.http import HttpResponse

# Create your views here.
def blogHome(request):
    return HttpResponse('this is blog home')

def blogPost(request,slug):
    return HttpResponse(f'this is blogpost: {slug}')