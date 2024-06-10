from rest_framework import serializers

from .models import Product, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True
    )

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'status', 'user']

    def create(self, validated_data):
        # Extract uploaded images from validated data
        uploaded_images = validated_data.pop('uploaded_images', [])

        # Create the product instance
        product = Product.objects.create(**validated_data, user=self.context['request'].user)

        # Create ProductImage instances for each uploaded image
        for image in uploaded_images:
            ProductImage.objects.create(product=product, image=image)

        return product


