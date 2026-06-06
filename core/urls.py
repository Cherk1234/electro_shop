from django.contrib import admin
from django.urls import path
from catalog.views import product_list, create_order, track_order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list, name='index'),
    path('api/create-order/', create_order, name='create_order'),
    path('api/track-order/', track_order, name='track_order'),
]
