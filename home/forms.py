from django import forms
from blog.models import Post

# works as mediator between table and data

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content','author')
