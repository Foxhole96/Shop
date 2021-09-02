from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', home, name='base'),
    path('catalog/0/<slug:category_slug>', cat_detail, name='category'),
    path('product/info/<slug:product_slug>', show_product, name='product'),
    path('chapter/<slug:singlepages_slug>/', pages, name='singlepages'),
    path('vendors/<slug:vendor_slug>/', show_vendor, name='vendor'),
    path('vendors/', all_vendors, name='all_vendors'),
    path('catalog/', ShopHome.as_view(), name='all_prods'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

