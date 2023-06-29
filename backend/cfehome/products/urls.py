from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.ProductDetailsAPIView.as_view(), name='product-detail'),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name='product-edit'),
    path('<int:pk>/delete/', views.ProductDeleteAPIView.as_view()),
    path('', views.ProductListCreatAPIView.as_view(), name='product-list')
]
