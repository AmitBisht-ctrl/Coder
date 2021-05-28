from django import forms
from blog.models import Post

# works as mediator between table and data

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content','author')

        # widgets = {
        #     # 'title': forms.TextInput(attrs={'class':'form-conrtol','placeholder':'Give a title to your blog'}),
        #     # 'author': forms.TextInput(attrs={'class':'form-conrtol','placeholder':"Author's Name here"}),
        #     'content': forms.TextInput(attrs={'class':'form-conrtol','placeholder':'Write your Content here...'})
        # }
