from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from datetime import datetime, timedelta

from .models import Product
from .permissions import SellerPermission
from .serializers import ProductSerializer

class ProductPostView(CreateAPIView):
    permission_classes=[IsAuthenticated, SellerPermission]
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = ProductSerializer

class ProductsGetView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer

    def get_queryset(self):
        
        uid = self.request.GET.get('user')

        if uid:
            return Product.objects.filter(user=uid)
        
        else:
            return Product.objects.filter(created_at__gte=datetime.today()-timedelta(days=3))

class ProductGetView(RetrieveAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        pid = self.request.GET.get('pid')
        return Product.objects.get(pk=pid)