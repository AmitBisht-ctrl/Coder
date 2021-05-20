from django.http.response import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from blog.models import BlogComment, Post
from django.contrib import messages

# from django.http import HttpResponse

# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request,'blog/blogHome.html',context)

def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post)
    print('comments:',comments)
    context = {'post': post,'comments':comments}
    return render(request,'blog/blogPost.html',context)

def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment','no value')
        postId = request.POST.get('postId','no value')
        post = Post.objects.get(id=postId)
        if len(comment) == 0:
            messages.error(request,'You can not make empty comments')
            return redirect(f'/blog/{post.slug}')
        user = request.user


        comment = BlogComment(comment=comment,user=user,post=post)
        comment.save()
        messages.success(request,'Your comment has been posted successfully')
    return redirect(f'/blog/{post.slug}')