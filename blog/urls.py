from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', BlogHome.as_view(), name='base_blog'),
    path('<slug:post_slug>', post_detail, name='post')
]

