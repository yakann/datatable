from django.urls import path

from orders.views import get_orders

urlpatterns = [
    path('static', get_orders, name='datatable_static'),
]