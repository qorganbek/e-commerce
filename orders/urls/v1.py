from rest_framework import routers
from orders import views

r = routers.DefaultRouter()

r.register(r'orders', views.OrderViewSet)
r.register(r'order-item', views.OrderItemViewSet)

urlpatterns = r.urls
