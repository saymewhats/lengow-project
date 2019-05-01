from django.shortcuts import render
from orders.models import Order
from django.http import HttpResponse


def get_orders(request):
    try:
        orders = Order.objects.all()
    except Order.DoesNotExist:
        return HttpResponse(status=404)

    return render(request, 'orders/list_orders.html', {'orders': orders})