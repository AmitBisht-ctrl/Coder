from django.http.response import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from blog.models import BlogComment, Post
from django.contrib import messages
from blog.templatetags import extras

# from django.http import HttpResponse

# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request,'blog/blogHome.html',context)
    
def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post,parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    repDict = {}
    for reply in replies:
        if reply.parent.sno not in repDict:
            repDict[reply.parent.sno] = [reply]
        else:
            repDict[reply.parent.sno].append(reply)

    print('final reply: ',repDict,'\nReplies: ',replies,'\nparent comment: ',comments)
    context = {'post': post,'comments': comments, 'repDict':repDict}
    return render(request,'blog/blogPost.html',context)

def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        parentSno = request.POST.get('parentSno')
        postId = request.POST.get('postId')
        print('postId:',postId)
        post = Post.objects.get(id=postId)
        if len(comment) == 0:
            messages.error(request,'You can not make empty comments')
            return redirect(f'/blog/{post.slug}')
        user = request.user
        print(parentSno)
        if parentSno:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment,user=user,post=post,parent=parent)

        else:
            comment = BlogComment(comment=comment,user=user,post=post)

        comment.save()
        messages.success(request,'Your comment has been posted successfully')
    return redirect(f'/blog/{post.slug}')