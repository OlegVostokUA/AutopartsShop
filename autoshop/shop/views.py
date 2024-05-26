from django.shortcuts import render, get_object_or_404
from .models import Category, Component, ComponentPhoto


def component_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    components = Component.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        components = components.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'components': components,
    }

    return render(request, 'shop/component/list.html', context)


def component_detail(request, id, slug):
    component = get_object_or_404(Component,
                                  id=id,
                                  slug=slug,
                                  available=True)
    context = {
        'component': component
    }

    return render(request, 'shop/component/detail.html', context)




