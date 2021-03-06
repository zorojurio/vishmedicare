# Generated by Django 3.1 on 2020-08-05 16:55

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('meta_description', models.TextField(blank=True, null=True)),
                ('key_words', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('facebook_image', models.ImageField(blank=True, null=True, upload_to='facebook_products/')),
            ],
        ),
    ]
