from django.urls import path

from . import views

urlpatterns = [
    path('', views.BidView.as_view(), name="bid"),
    path('get/', views.BidsGetView.as_view(), name="bid_get")
]