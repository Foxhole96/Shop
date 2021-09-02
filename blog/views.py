from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import *
from main.models import Category
from django.http import HttpResponse, HttpResponseNotFound, Http404


#def blog_home(request, template='blog/blog.html'):
#    top_post = Posts.objects.all().order_by('-date')
#    content = {
#        'meta_title': 'Блог компании Sonet',
#       'meta_description': 'Блог компании Sonet - мета описание',
#        'last_post': top_post,
#    }
#
#   return render(request, template, content)


class BlogHome(ListView):
    paginate_by = 6
    model = Posts
    template_name = 'blog/blog.html'
    context_object_name = 'last_post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meta_title'] = 'Блог компании Sonet'
        context['meta_description'] = 'Все товары интернет магазина Sonet'
        context['title'] = 'Блог компании Sonet - мета описание'
        return context

    def get_queryset(self):
        return Posts.objects.all().order_by('date')


def post_detail(request, post_slug, template='blog/post_detail.html'):
    post_slug = get_object_or_404(Posts, slug=post_slug)
    posts = Posts.objects.all()
    last_post = Posts.objects.order_by('-id')[:3]
    context = {
        'post': post_slug,
        'meta_tags': posts,
        'last_post': last_post,
    }

    return render(request, template, context)

