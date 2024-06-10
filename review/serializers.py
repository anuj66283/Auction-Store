from .models import Review
from store.models import ProductHistory

from rest_framework import serializers

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['rating', 'review']
        read_only_fields = ['id', 'buyer', 'seller', 'product', 'review_date']
    
    def validate(self, data):
        buyer = self.context['request'].user
        pid = self.context.get('pid')

        product = ProductHistory.objects.filter(product=pid, buyer=buyer)

        if not product:
            return serializers.ValidationError("You need to buy the product to make review")
    
        return data

    def create(self, validated_data):
        buyer = self.context['request'].user
        pid = self.context.get('pid')

        product = ProductHistory.objects.get(product=pid, buyer=buyer)


        Review.objects.create(buyer=buyer,
                                   seller=product.product.user,
                                   product=product.product,
                                   rating=validated_data.get("rating"),
                                   review=validated_data.get("review"))

