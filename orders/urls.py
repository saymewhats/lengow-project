from django.contrib import admin
from django.urls import path, include
from orders.admin import admin_site
from orders import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register(r'orders', views.OrderViewSet)

urlpatterns = [
    path('admin/', admin_site.urls),
    path('list_order/', views.get_orders, name='list_order'),
    path('order/<int:id>/', views.get_order, name='get_order'),
    path('order/delete/<int:id>/', views.del_order, name='del_order'),
    path('list_order_filter/', views.get_orders_filter, name='list_order_filter'),
    path('add_order/', views.add_order, name='add_order'),
    path('', include(routers.urls)),
    path('api-order/', include('rest_framework.urls', namespace="rest_framework"))
]
