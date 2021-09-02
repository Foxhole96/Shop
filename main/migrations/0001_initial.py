# Generated by Django 3.2.6 on 2021-09-02 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Имя категории')),
                ('slug', models.SlugField(unique=True)),
                ('meta_title', models.CharField(max_length=120, null=True, unique=True, verbose_name='Мета заголовок')),
                ('meta_description', models.CharField(max_length=250, null=True, unique=True, verbose_name='Мета описание')),
                ('image', models.ImageField(default='default image', upload_to='main/image/')),
                ('alt_img', models.CharField(blank=True, max_length=255, null=True, verbose_name='Alt')),
                ('description', models.TextField(blank=True)),
                ('short_description', models.CharField(max_length=255, null=True, verbose_name='Краткое описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'db_table': 'category',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='SinglePages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='Slug')),
                ('meta_title', models.CharField(max_length=120, null=True, unique=True, verbose_name='Мета заголовок')),
                ('meta_description', models.CharField(max_length=250, null=True, unique=True, verbose_name='Мета описание')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
                'db_table': 'singlepages',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='Slug')),
                ('image', models.ImageField(blank=True, null=True, upload_to='main/image/', verbose_name='Изображение')),
                ('alt_img', models.CharField(blank=True, max_length=255, null=True, verbose_name='Alt')),
                ('meta_title', models.CharField(max_length=120, null=True, unique=True, verbose_name='Мета заголовок')),
                ('meta_description', models.CharField(max_length=250, null=True, unique=True, verbose_name='Мета описание')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
                'db_table': 'vendor',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('sku', models.CharField(max_length=15, null=True, unique=True, verbose_name='Артикул')),
                ('availability', models.BooleanField(default=True, verbose_name='Наличие')),
                ('meta_title', models.CharField(max_length=120, null=True, unique=True, verbose_name='Мета заголовок')),
                ('meta_description', models.CharField(max_length=250, null=True, unique=True, verbose_name='Мета описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='main/image/', verbose_name='Изображение')),
                ('alt_img', models.CharField(blank=True, max_length=255, null=True, verbose_name='Alt')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('short_description', models.CharField(max_length=255, null=True, verbose_name='Краткое описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('characters', models.TextField(null=True, verbose_name='Характеристики')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.category', verbose_name='Категория')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.vendor', verbose_name='Производитель')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'db_table': 'product',
                'ordering': ['title'],
            },
        ),
    ]