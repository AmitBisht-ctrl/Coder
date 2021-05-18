from django.db import models
from django.db.models.signals import pre_save
from Coder.utils import unique_slug_generator

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.CharField(max_length=25)
    slug = models.SlugField(unique=True,blank=True)
    timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + ' by ' + self.author 

    class Meta:
        unique_together = ['title','slug']



# source for slug-maker: youtube channel: ishwar jangid

# may remove sender since we are not using it(not in pre_save though)
def slug_generator(instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator,sender=Post)