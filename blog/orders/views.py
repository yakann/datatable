from django.db.models import Sum, F, DecimalField
from django.shortcuts import render

from orders.models import Order


def get_orders(request, *args, **kwargs):
    orders_qs = Order.objects.all().annotate(
        total_amount=Sum(
            F('orderline__unit_price') * F('orderline__quantity'),
            output_field=DecimalField())
    )

    return render(
        request=request,
        template_name="datatable/datatable-static.html",
        context={
            "order_list": orders_qs
        })