from django.shortcuts import render, get_object_or_404
from .models import Category, Component, ComponentPhoto
from taggit.models import Tag


def component_list(request, category_slug=None, tag_slug=None):
    category = None
    tag = None

    categories = Category.objects.filter(parent=None)

    #categories = Category.objects.all()
    components = Component.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        components = components.filter(category=category)

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        components = components.filter(tags__in=[tag])
    context = {
        'category': category,
        'categories': categories,
        'components': components,
        'tag': tag
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




