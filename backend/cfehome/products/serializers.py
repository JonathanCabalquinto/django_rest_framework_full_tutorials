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

    class Meta:
        model = Product
        fields = [
            'edit_url',
            'view_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'discount'
        ]
