from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)

    def get_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()

    # url = serializers.SerializerMethodField(read_only=True)

    # Append URL to each product to view it
    # def get_url(self, obj):
    #     request = self.context.get('request')
    #     if request is None:
    #         return None
    #     return reverse("product-detail", kwargs={'pk': obj.pk}, request=request)

    # Shorter way
    view_url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )

    edit_url = serializers.SerializerMethodField(read_only=True)

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={'pk': obj.pk}, request=request)

    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Product
        fields = [
            'email',
            'edit_url',
            'view_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'discount'
        ]

    def create(self, validated_data):
        # email = validated_data.pop('email')
        obj = super().create(validated_data)
        # print(email, obj)
        return obj

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title')
        return super().update(instance, validated_data)
