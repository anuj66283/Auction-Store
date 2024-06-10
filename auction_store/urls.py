"""
URL configuration for auction_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views  as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include("account.urls")),
    path('api/v1/store/', include("store.urls")),
    path('api/v1/bid/', include("bid.urls")),
    path('api/v1/review/', include("review.urls")),
    path('api/v1/token/', jwt_views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', jwt_views.CustomTokenRefreshView.as_view(), name='token_refresh'),
]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
