from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.component_list, name='component_list'),
    path('search-results/', views.search_results, name='search_results'), # search_results
    path('about-contacts/', views.about_contacts, name='about_contacts'), # search_results
    path('<slug:category_slug>/', views.component_list, name='component_list_by_category'),
    path('tag/<slug:tag_slug>/', views.component_list, name='component_list_by_tag'),
    path('<int:id>/<slug:slug>/', views.component_detail, name='component_detail'),

]