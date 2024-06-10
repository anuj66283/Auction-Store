from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .models import Review
from .serializers import ReviewSerializer

from store.permissions import BuyerPermission


# Create your views here.

class ReviewView(APIView):
    permission_classes = [BuyerPermission]
    
    def post(self, request, pid):
        review = ReviewSerializer(data=request.data)

        if review.is_valid():
            review.save()
            return Response(review.data, status=status.HTTP_200_OK)

        return Response(review.errors, status=status.HTTP_404_NOT_FOUND)
    
class GetReview(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ReviewSerializer

    def get_queryset(self):
        bid = self.request.GET.get("bid")
        sid = self.request.GET.get("sid")

        if bid:
            return Review.objects.filter(buyer=bid)
        if sid:
            return Review.objects.filter(seller=sid)
        
        return Response("provide bid or sid", status=status.HTTP_204_NO_CONTENT)



