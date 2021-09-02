from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from datetime import date
from django.shortcuts import render
from django.urls import reverse


class Category(models.Model):
    class Meta:
        db_table = 'category'
        ordering = ['title']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    title = models.CharField(max_length=255, verbose_name='Имя категории', db_index=True)
    slug = models.SlugField(unique=True)
    meta_title = models.CharField(max_length=120, verbose_name='Мета заголовок', null=True, unique=True)
    meta_description = models.CharField(max_length=250, verbose_name='Мета описание', null=True, unique=True)
    image = models.ImageField(upload_to='main/image/', default='default image')
    alt_img = models.CharField(verbose_name='Alt', max_length=255, null=True, blank=True)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=255, verbose_name='Краткое описание', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})


class Product(models.Model):
    class Meta:
        db_table = 'product'
        ordering = ['title']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.PROTECT)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True, db_index=True)
    sku = models.CharField(max_length=15, verbose_name='Артикул', null=True, unique=True)
    availability = models.BooleanField(default=True, verbose_name='Наличие')
    meta_title = models.CharField(max_length=120, verbose_name='Мета заголовок', null=True, unique=True)
    meta_description = models.CharField(max_length=250, verbose_name='Мета описание', null=True, unique=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='main/image/', null=True, blank=True)
    alt_img = models.CharField(verbose_name='Alt', max_length=255, null=True, blank=True)
    description = models.TextField(verbose_name='Описание', null=True)
    short_description = models.CharField(max_length=255, verbose_name='Краткое описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    vendor = models.ForeignKey('Vendor', verbose_name='Производитель', on_delete=models.CASCADE)
    characters = models.TextField(verbose_name='Характеристики', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})


class SinglePages(models.Model):
    class Meta:
        db_table = 'singlepages'
        ordering = ['title']
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    title = models.CharField(max_length=150, verbose_name='Название', unique=True)
    slug = models.SlugField(max_length=150, verbose_name='Slug', unique=True)
    meta_title = models.CharField(max_length=120, verbose_name='Мета заголовок', null=True, unique=True)
    meta_description = models.CharField(max_length=250, verbose_name='Мета описание', null=True, unique=True)
    description = models.TextField(verbose_name='Описание', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('singlepages', kwargs={'singlepages_slug': self.slug})


class Vendor(models.Model):
    class Meta:
        db_table = 'vendor'
        ordering = ['title']
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    title = models.CharField(max_length=150, verbose_name='Название', unique=True)
    slug = models.SlugField(max_length=150, verbose_name='Slug', unique=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='main/image/', null=True, blank=True)
    alt_img = models.CharField(verbose_name='Alt', max_length=255, null=True, blank=True)
    meta_title = models.CharField(max_length=120, verbose_name='Мета заголовок', null=True, unique=True)
    meta_description = models.CharField(max_length=250, verbose_name='Мета описание', null=True, unique=True)
    description = models.TextField(verbose_name='Описание', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('vendor', kwargs={'vendor_slug': self.slug})




