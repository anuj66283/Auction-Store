from .models import BuyerUser, SellerUser

from rest_framework import serializers
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class UserRegistration(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=60, min_length=8, write_only=True)
    password2 = serializers.CharField(max_length=60, min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2']

class BuyerRegistration(serializers.ModelSerializer):
    buyer = UserRegistration()

    class Meta:
        model = BuyerUser
        fields = ['buyer', 'profile']

    def create(self, validated_data):
        print(validated_data)
        user_b = validated_data.pop('buyer')
        
        if user_b['password1']!=user_b['password2']:
            raise serializers.ValidationError("Passwords do not match")
        
        p1 = user_b.pop('password1')
        user_b.pop('password2')

        buyer = CustomUser.objects.create(**user_b)
        buyer.set_password(p1)
        buyer.save()

        return BuyerUser.objects.create(buyer=buyer, **validated_data)



class SellerRegistration(serializers.ModelSerializer):
    seller = UserRegistration()

    class Meta:
        model = SellerUser
        fields = ['seller', 'district', 'full_address', 'profile']
    
    def create(self, validated_data):
        user_b = validated_data.pop('seller')
        
        if user_b['password1']!=user_b['password2']:
            raise serializers.ValidationError("Passwords do not match")
        
        p1 = user_b.pop('password1')
        user_b.pop('password2')

        seller = CustomUser.objects.create(**user_b)
        seller.set_password(p1)
        seller.is_buyer=False
        seller.save()

        return SellerUser.objects.create(seller=seller, **validated_data)

class CodeSerializer(serializers.Serializer):
    code = serializers.IntegerField()
    username = serializers.CharField(max_length=40)