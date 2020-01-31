from django.urls import path
from . views import Home
from Ecommerce import settings
from django.conf.urls.static import static
from cart.views import add_to_cart, remove_from_cart

from  . views import Home
app_name = 'mainapp'

urlpatterns = [

    path('', Home.as_view(), name='Home'),
    path('cart/<slug>', add_to_cart, name='cart'),
    path('remove/<slug>', remove_from_cart, name='remove-cart')


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)