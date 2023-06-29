from rest_framework.routers import DefaultRouter
from products.viewsets import ProductViewSets, ProductGenericViewSet


# All View Sets
# router = DefaultRouter()
# router.register('products-abc', ProductViewSets, basename='products')

# print(router.urls)
# urlpatterns = router.urls


# Specific View Sets

router = DefaultRouter()
router.register('product-abc', ProductGenericViewSet, basename='products')
print(router.urls)
urlpatterns = router.urls
