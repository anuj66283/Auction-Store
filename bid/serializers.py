from .models import Bid

from rest_framework import serializers

class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ['price', 'product']
        read_only_field = ['user', 'bid_date']

    def validate(self, data):
        usr = self.context['request'].user

        pdt = data['product']

        if pdt.status != "available":
            return serializers.ValidationError("Product not avaliable")

        bid = Bid.objects.filter(product=pdt.id).order_by('-bid_date').first()

        if bid:
            if bid.user == usr:
                raise serializers.ValidationError("Wait for others to bid first")
            
            if bid.price >= data['price']:
                raise serializers.ValidationError("Bid a higher amount")
        else:
            if data['price'] <= pdt.price:
                raise serializers.ValidationError("Bid a higher amount")
            
        return data
    
    def create(self, validated_data):
        usr = self.context['request'].user
        bid = Bid.objects.create(user=usr, **validated_data)

        return bid
