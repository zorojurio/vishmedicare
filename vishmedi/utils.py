from django.utils.text import slugify
import os
from random import randint
import random
import string

def get_filename(path):
    return os.path.basename(path)  # returns the final component of the path name

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def random_number_generator(size=20, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def get_filename_ext(filepath):
    # getting the file name from the file directory
    base_name = os.path.basename(filepath)
    # splitting the extention and the file name
    name, ext = os.path.splitext(base_name)
    return name, ext

def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=10)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug