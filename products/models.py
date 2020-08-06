from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.urls import reverse
from django.db.models.signals import post_save, pre_save
from vishmedi.utils import unique_slug_generator, get_filename_ext
import random

def image_upload_to(instance, filename):
    slug = instance.slug
    random_name = random.randint(1, 391541656)
    basename, file_extension = get_filename_ext(filename)
    new_file_name = f"{slug}-{random_name}{file_extension}"
    return f"products/{slug}/{new_file_name}"
    

def facebook_image_upload_to(instance, filename):
    slug = instance.slug
    random_name = random.randint(1, 391541656)
    basename, file_extension = get_filename_ext(filename)
    new_file_name = f"{slug}-{random_name}{file_extension}"
    return f"products/facebook/{slug}/{new_file_name}"


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, blank=True, null=True, max_digits=7)
    description = RichTextUploadingField(blank=True, null=True)
    active = models.BooleanField(default=True)
    meta_description = models.TextField(blank=True, null=True)
    key_words = models.TextField(blank=True, null=True)
    timestamp = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    slug = models.SlugField(blank=True, unique=True)
    product_image = models.ImageField(upload_to=image_upload_to, blank=True, null=True)
    facebook_image = models.ImageField(upload_to=facebook_image_upload_to, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_product_image(self):
        if self.product_image:
            return self.product_image.url
    
    def get_facebook_image(self):
        if self.facebook_image:
            return self.facebook_image.url

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug': self.slug})

# generating unique slug
def product_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_reciever, sender=Product)