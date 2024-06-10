from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView

from .serializers import BuyerRegistration, SellerRegistration, CodeSerializer

CustomUser = get_user_model()

# Create your views here.

class BuyerRegisterView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = BuyerRegistration

class SellerRegisterView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = SellerRegistration

class VerifyView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        un_code = CodeSerializer(data=request.data)

        if un_code.is_valid():
            code = un_code.validated_data['code']
            username = un_code.validated_data['username']
            
            print(request.user)
            usr = CustomUser.objects.filter(username=username, code=code)

            if usr:
                usr = usr[0]
                usr.is_verified = True
                usr.code = 0
                usr.save()

                return Response({"msg":"Email verified successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"msg":"Invalid username or code"}, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({"msg":"Invalid data"}, status=status.HTTP_400_BAD_REQUEST)
