from products import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'product-images', views.ProductImageViewSet)

urlpatterns = router.urls
