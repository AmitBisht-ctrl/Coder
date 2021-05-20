from django.contrib import admin
from blog.models import Post, BlogComment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post
        prepopulated_fields = {'slug':('title','author')}
        

# we have to send the data in a tupple
admin.site.register(Post,PostAdmin)
admin.site.register(BlogComment)
