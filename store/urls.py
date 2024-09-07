from django.urls import path
from . import views

urlpatterns = [
    path('',views.tienda,name="Tienda"),
    path('<slug:category_slug>/',views.tienda , name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/',views.product_detail, name='product_detail'),
]