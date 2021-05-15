from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('this is home')

def about(index):
    return HttpResponse('this is about')

def contact(request):
    return HttpResponse('this is contact')