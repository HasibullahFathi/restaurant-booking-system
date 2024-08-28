from . import views
from django.urls import path

urlpatterns = [

    path('', views.menu_category_list, name='menu_category_list'),
    path('create/category/', views.create_menu_category, name='create_menu_category'),
    path('create/item/', views.create_menu_item, name='create_menu_item'),
    path('edit/<int:category_id>/', views.edit_menu_category, name='edit_menu_category'),
    path('delete/<int:category_id>/', views.delete_menu_category, name='delete_menu_category'),
    
]