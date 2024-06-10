from django.urls import path
from . import views

urlpatterns = [
    path('buyer/register/', views.BuyerRegisterView.as_view(), name='buyer_register'),
    path('seller/register/', views.SellerRegisterView.as_view(), name='seller_register'),
    path('verify/', views.VerifyView.as_view(), name="verify")
]
