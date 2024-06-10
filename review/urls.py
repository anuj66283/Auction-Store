from django.urls import path

from . import views

urlpatterns = [
    path('<str:pid>/', views.ReviewView.as_view(), name="review")
]