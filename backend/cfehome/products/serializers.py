from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validators import unique_product_title, validate_title_no_hello


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

    # email = serializers.EmailField(write_only=True)

    title = serializers.CharField(
        validators=[validate_title_no_hello, unique_product_title])
    # name = serializers.CharField(source='title', read_only=True)

    class Meta:
        model = Product
        fields = [
            # 'user',
            # 'email',
            'edit_url',
            'view_url',
            # 'name',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'discount'
        ]

    # def create(self, validated_data):
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     # print(email, obj)
    #     return obj

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title')
    #     return super().update(instance, validated_data)

    # Custom Serilizer First Approach
    # 1 Approch

    # def validate_title(self, value):
    #     request = self.context.get('request')
    #     qs = Product.objects.filter(title__exact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(
    #             f"{value} is already a product name")
    #     return True

    # Note: exact and iexact
