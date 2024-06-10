from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.ProductPostView.as_view(), name="create_product"),
    path('products/', views.ProductsGetView.as_view(), name="products"), 
    path('product/', views.ProductGetView.as_view(), name='product')
]