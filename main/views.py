from django.shortcuts import render, get_object_or_404
from .models import *
from blog.models import *
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpResponseNotFound, Http404

menu = ["Доставка и оплата", "Гарантия", "Контакты", "О нас"]


def home(request, template='main/home.html'):
    """Вивід інформації на головну сторінку"""
    top_post = Posts.objects.order_by('-id')[:3]
    top_products = Product.objects.order_by('-id')[:8]
    page_data = SinglePages.objects.all().order_by('id')
    context = {

        'last_post': top_post,
        'last_products': top_products,
        'title': 'Главная страница',
        'footer_menu': menu,
        'page_data': page_data,
    }
    return render(request, template, context=context)


def cat_detail(request, category_slug, template='main/cat_detail.html'):
    """Сторінка конкретної категорії"""
    category_slug = get_object_or_404(Category, slug=category_slug)
    product_in_cat = Product.objects.filter(category=category_slug)
    title = Category.objects.all()
    all_prods = Product.objects.order_by('title')

    context = {
        'category': category_slug,
        'product_in_cat': product_in_cat,
        'meta_tags': title,
        'all_prods': all_prods,
    }

    return render(request, template, context)


def pages(request, singlepages_slug, template='main/singlepage.html'):
    page_slug = get_object_or_404(SinglePages, slug=singlepages_slug)

    context = {
        'page_slug': page_slug,

    }

    return render(request, template, context)


def show_vendor(request, vendor_slug, template='main/vendors.html'):
    vendor_slug = get_object_or_404(SinglePages, slug=vendor_slug)

    context = {
        'vendor_slug': vendor_slug,

    }

    return render(request, template, context)


def all_vendors(request, template='main/vendor_base.html'):
    all_vendors = Vendor.objects.all()

    context = {
        'all_vendors': all_vendors,
        'meta_title': 'Все производители',
        'meta_description': 'Все производители интернет магазина Sonet',

    }

    return render(request, template, context)


class ShopHome(ListView):
    paginate_by = 12
    model = Product
    template_name = 'main/shop.html'
    context_object_name = 'all_prods'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meta_title'] = 'Все товары интернет магазина Sonet'
        context['meta_description'] = 'Все товары интернет магазина Sonet'
        context['title'] = 'Интернет магазин Sonet'
        return context

    def get_queryset(self):
        return Product.objects.filter(availability=True).order_by('price')


def show_product(request, product_slug, template='main/product_page.html'):
    product_slug = get_object_or_404(Product, slug=product_slug)
    product_meta = Product.objects.all()
    vendor = Vendor.objects.all()

    context = {
        'product': product_slug,
        'product_meta': product_meta,
        'vendor' : vendor,

    }

    return render(request, template, context)

