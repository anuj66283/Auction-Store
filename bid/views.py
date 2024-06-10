from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Bid
from .serializers import BidSerializer
from store.permissions import BuyerPermission

class BidView(APIView):
    permission_classes=[IsAuthenticated, BuyerPermission]
    
    def post(self, request):
        bid = BidSerializer(data = request.data, context={'request':request})

        if bid.is_valid():
            bid.save()
            return Response(bid.data, status=status.HTTP_201_CREATED)
        
        return Response(bid.errors, status=status.HTTP_400_BAD_REQUEST)

class BidsGetView(ListAPIView):
    serializer_class = BidSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        pid = self.request.GET.get('pid')
    
        if pid:
            return Bid.objects.filter(product=pid)

        return Response("provide pid", status=status.HTTP_204_NO_CONTENT)