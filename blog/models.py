from django.db import models
from django.shortcuts import render, reverse, redirect

from ckeditor_uploader.fields import RichTextUploadingField


# from django. import User

class Post(models.Model):
    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft'),
    )
    title = models.CharField(max_length=300)
    description = models.TextField(verbose_name='توضیحات')
    thumbnail = models.ImageField(upload_to="images")
    date_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])  # /blog/8
