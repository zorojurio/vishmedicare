from django.contrib import admin
from products.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display  = [ 'title', 'price']
    list_display_links = [ 'title', 'price']
    search_fields = [ 'title', 'price']


admin.site.register(Product, ProductAdmin)
