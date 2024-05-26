from django.contrib import admin
from .models import Component, Category, ComponentPhoto


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)


class ComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'price', 'currency', 'available')
    list_editable = ('price', 'available', 'currency')
    ordering = ('name',)
    list_filter = ('name', 'category', 'brand', 'price', 'available')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Component, ComponentAdmin)
admin.site.register(ComponentPhoto)
