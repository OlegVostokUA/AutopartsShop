from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.component_list, name='component_list'),
    path('<slug:category_slug>/', views.component_list, name='component_list_by_category'),
    path('<int:id>/<slug:slug>/', views.component_detail, name='component_detail')
]