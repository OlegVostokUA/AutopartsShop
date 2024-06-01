from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddComponentForm
from shop.models import Component


@require_POST
def cart_add(request, component_id):
    cart = Cart(request)
    component = get_object_or_404(Component, id=component_id)
    form = CartAddComponentForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(component=component,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, component_id):
    cart = Cart(request)
    component = get_object_or_404(Component, id=component_id)
    cart.remove(component)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)

    for item in cart:
        item['update_quantity_form'] = CartAddComponentForm(
            initial={'quantity': item['quantity'],
                     'update': True})
    return render(request,
                  'cart/detail.html',
                  {'cart': cart})
