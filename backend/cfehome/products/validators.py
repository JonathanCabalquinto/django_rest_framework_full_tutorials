# 2 Approach Validators
from rest_framework import serializers
from .models import Product

# 3 Approach
from rest_framework.validators import UniqueValidator


def validate_title(value):
    qs = Product.objects.filter(title__exact=value)
    if qs.exists():
        raise serializers.ValidationError(
            f"{value} is already a product name")
    return True


def validate_title_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError(
            f"{value} is not allowed")


unique_product_title = UniqueValidator(queryset=Product.objects.all())
