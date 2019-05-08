from django.shortcuts import render
from orders.models import Order
from django.http import HttpResponse, HttpResponseRedirect
from orders.forms import OrderForm, FilterForm
from rest_framework import viewsets
from orders.serializers import OrderSerializer


def get_orders(request):
    """This method allow get all orders"""
    try:
        orders = Order.objects.all()
        form_filter = FilterForm()
        contains = {
            'form_filter': form_filter,
            'orders': orders
        }
    except Order.DoesNotExist:
        return HttpResponse(status=404)

    return render(request, 'orders/list_orders.html', contains)


def get_orders_filter(request):
    """Allow to get all orders with filter"""
    if request.method == 'POST':
        form = FilterForm(request.POST)
        form.is_valid()
        list_order = create_query_filter(form)
        return render(request, 'orders/list_orders.html', {'orders': list_order, 'form_filter': form})


def get_order(request, id):
    """get just one order for display details and modify order"""
    form_filter = FilterForm()
    order = Order.objects.get(id=id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            contains = {
                'orders': Order.objects.all(),
                'form_filter': form_filter
            }
            return render(request, 'orders/list_orders.html', contains)
    else:
        try:
            form = OrderForm(instance=order)
        except Order.DoesNotExist:
            return HttpResponse(status=404)

    return render(request, 'orders/order.html', {'formOrder': form})


def del_order(request, id):
    """allow to delete order"""
    order = Order.objects.get(id=id)
    try:
        order.delete()
        return render(request, 'orders/list_orders.html', {'orders': Order.objects.all()})
    except Order.DoesNotExist:
        return HttpResponse(status=404)


def add_order(request):
    """Allow to add a new order"""
    form_filter = FilterForm()
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        form.save()
        contains = {
            'orders': Order.objects.all(),
            'form_filter': form_filter
        }
        return render(request, 'orders/list_orders.html', contains)

    return render(request, 'orders/add_order.html', {'form': form})


def create_query_filter(form):
    field = form.cleaned_data.get('field')
    if field == 'marketplace':
        return Order.objects.filter(marketplace__contains=form.cleaned_data.get('search'))
    if field == 'amout':
        return Order.objects.filter(amount__contains=form.cleaned_data.get('search'))
    if field == 'shipping':
        return Order.objects.filter(shipping__contains=form.cleaned_data.get('search'))
    if field == 'address':
        return Order.objects.filter(address__contains=form.cleaned_data.get('search'))
    if field == 'last_name':
        return Order.objects.filter(last_name__contains=form.cleaned_data.get('search'))
    if field == 'city':
        return Order.objects.filter(city__contains=form.cleaned_data.get('search'))


class OrderViewSet(viewsets.ModelViewSet):
    """API endpoint that allows order to be viewed or edited"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


