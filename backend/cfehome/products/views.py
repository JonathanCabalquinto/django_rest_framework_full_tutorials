from rest_framework import generics, mixins
from .models import Product
from .serializers import ProductSerializer

from api.permissions import IsStaffEditorPermission
from api.authentication import TokenAuthentication
from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin


class ProductDetailsAPIView(
    UserQuerySetMixin,
        StaffEditorPermissionMixin,
        generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListCreatAPIView(
        UserQuerySetMixin,
        StaffEditorPermissionMixin,
        generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # email = serializer.validated_data.get('email')
        # if email is not None:
        #     email = serializer.validated_data.pop('email')

        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')

        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)

    # def get_queryset(self, *args, **kwargs):
    #     # request = self.request
    #     # print(request.user)
    #     # return super().get_queryset(*args, **kwargs)
    #     qs = super().g`et_queryset(*args, **kwargs)
    #     request = self.request
    #     user = request.user

    #     return qs.filter(user=request.`user)


class ProductUpdateAPIView(UserQuerySetMixin, StaffEditorPermissionMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProductDeleteAPIView(UserQuerySetMixin, StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


class ProductMixinViews(
    UserQuerySetMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')

        if content is None:
            content = "Test 12345"
        serializer.save(content=content)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


product_mixin_views = ProductMixinViews.as_view()
