from django.http.response import HttpResponse
from django.shortcuts import render
from home.models import Contact
from django.contrib import messages
from blog.models import Post

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def about(request):
    return render(request,'home/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) <= 2 or len(email) <= 5 or len(phone) < 10 or len(content) <=5:
            messages.error(request,'Please enter all your details correctly.')
            return render(request,'home/contact.html')
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request,'Your form has been submitted successfully.')
    return render(request,'home/contact.html')


def search(request):
    query = request.GET['query']
    if len(query) > 80 or len(query) <= 2:
        allpost = []
    else:
        allposttitle = Post.objects.filter(title__icontains=query)
        allpostcontent = Post.objects.filter(content__icontains=query)
        allpost = allposttitle.union(allpostcontent)
        print(allpost)

    if len(allpost) == 0:
            messages.warning(request,'Sorry we could not find anything related to your query.')
            
    params = {'allPosts':allpost,'query':query}
    return render(request,'home/search.html',params)