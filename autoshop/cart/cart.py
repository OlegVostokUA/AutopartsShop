from decimal import Decimal
from django.conf import settings
from shop.models import Component


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, component, quantity=1, update_quantity=False):
        component_id = str(component.id)
        if component_id not in self.cart:
            self.cart[component_id] = {'quantity': 0,
                                       'price': str(component.price)}
        if update_quantity:
            self.cart[component_id]['quantity'] = quantity
        else:
            self.cart[component_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, component):
        component_id = str(component.id)
        if component_id in self.cart:
            del self.cart[component_id]
            self.save()

    def __iter__(self):
        component_ids = self.cart.keys()
        components = Component.objects.filter(id__in=component_ids)
        for comp in components:
            self.cart[str(comp.id)]['component'] = comp

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
