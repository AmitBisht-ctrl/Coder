
import string
import random
from django.utils.text import slugify

# source: youtube channel: ishwar jangid


# taking size=10 and char as default parameters chars will have all ascii lower cases and string digits 
# then we will generate a random string using these characters
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    # checking the existance of slug in the table
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()


    # if present then it will add 4 random chars to the end using random string generator
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug