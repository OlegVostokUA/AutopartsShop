from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['component']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'city', 'postal_code',
                    'created', 'updated', 'paid']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
