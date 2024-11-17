from django.urls import path, include
from .views import ProductViewSet, ProductDetail
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
]
