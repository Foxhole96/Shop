from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from datetime import date
from django.urls import reverse


class Posts(models.Model):

    class Meta:
        db_table = 'posts'
        ordering = ['title']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(unique=True)
    meta_title = models.CharField(max_length=120, verbose_name='Мета заголовок', null=True, unique=True)
    meta_description = models.CharField(max_length=250, verbose_name='Мета описание', null=True, unique=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='blog/image/', null=True, blank=True)
    alt_img = models.CharField(verbose_name='Alt', max_length=255, null=True, blank=True)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=255, verbose_name='Краткое описание', null=True)
    date = models.DateField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})