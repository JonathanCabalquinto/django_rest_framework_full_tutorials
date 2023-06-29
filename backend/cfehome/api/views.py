from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework import generics


# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     # model_data = Product.objects.all().order_by("?").last()

#     instance = Product.objects.all().order_by("?").first()
#     data = {}

#     if instance:
#         data = ProductSerializer(instance).data
#     else:
#         pass

#     return Response(data)


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # print(instance)
        return Response(serializer.data)
