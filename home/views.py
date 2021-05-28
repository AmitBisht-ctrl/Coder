from django.contrib.messages.constants import ERROR
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from home.forms import PostForm

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
            messages.error(request,'Sorry we could not find anything related to your query.')
            # messages.add_message(request,ERROR,'Sorry we could not find anything related to your query.',extra_tags='warning')
    params = {'allPosts':allpost,'query':query}
    return render(request,'home/search.html',params)


# Authentication API

def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameter 
        username= request.POST['Username']
        fname = request.POST['fname']
        lname = request.POST.get('lname','')
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        # Check the errorneous inputs

        if len(username) > 10 or len(username) < 2:
            messages.error(request,'Username must be less than 10 character or more than 2 characters')
            return redirect('home')


        if not username.isalnum():
            messages.error(request,'Username can only contain alphabets or numbers')
            return redirect('home')

        if pass1 != pass2:
            messages.error(request,'Passwords do not match')
            return redirect('home')


        # Create the user
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'Your Coder account has been successfully created.')
        # here home is the name of url of our base page 
        # using name just so that if in future we end up changing the url we will still have a working program
        return redirect('home')
        
    else:
        return HttpResponse('<h1>404 - Not Found </h1>')

def handlelogin(request):
    if request.method == 'POST':
        # Get the post parameter 
        username= request.POST['Username']
        passw = request.POST['password']
        
        user = authenticate(username=username, password=passw) 
        
        if user is not None:
            login(request, user)
            messages.success(request,"Successfully Logged In")

        else:
            messages.error(request,'Invalid Credentials. Please try again')
        
        return redirect('home')
        
def handlelogout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request,'Successfully Logged Out')
    return redirect('home')


def postblog(request):
    if request.method == "POST":
        title = request.POST.get('title','')
        author = request.POST.get('author','')
        content = request.POST.get('content','')

        print('title: ',title, '\nauthor:',author, '\ncontetn:',content)

        postBlog = Post(title=title, author=author, content=content)
        postBlog.save()
        print(postBlog.save())
        messages.success(request,"Successfully Posted Your Blog")

        return redirect('/postblog/')
    
    form = PostForm()
    return render(request,'home/postYourBlog.html',{'form':form})