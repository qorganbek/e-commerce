from rest_framework import routers
from seller_products import views

r = routers.DefaultRouter()
r.register(r'seller_product', views.SellerProductView)

urlpatterns = r.urls
