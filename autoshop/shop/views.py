from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Category, Component, ComponentPhoto, Contacts
from taggit.models import Tag
from cart.forms import CartAddComponentForm
from django.db.models import Q

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
    cart_component_form = CartAddComponentForm()
    context = {
        'component': component,
        'cart_component_form': cart_component_form
    }

    return render(request, 'shop/component/detail.html', context)


def search_results(request):
    query = request.GET.get('q')
    components = Component.objects.filter(Q(serial_number__icontains=query) | Q(name__icontains=query))

    context = {
        'components': components,
    }

    return render(request, 'shop/component/list.html', context)


def about_contacts(request):
    contacts = Contacts.objects.all()
    return render(request, 'shop/about.html', {'contacts': contacts[0]})

# class SearchResultsView(ListView):
#     model = Component
#     template_name = 'shop/component/list.html'
#
#     def get_queryset(self): # новый
#         query = self.request.GET.get('q')
#         object_list = Component.objects.filter(
#             Q(name__icontains=query) | Q(state__icontains=query)
#         )
#         return object_list