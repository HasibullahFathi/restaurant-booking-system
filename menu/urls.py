from django.urls import path
from . import views

urlpatterns = [
    path('create/category/', views.create_menu_category, name='create_menu_category'),
    path('create/item/', views.create_menu_item, name='create_menu_item'),
    path('delete/<int:category_id>/', views.delete_menu_category, name='delete_menu_category'),
    path('delete_item/<int:item_id>/', views.delete_menu_item, name='delete_menu_item'),
    path('edit/<int:category_id>/', views.edit_menu_category, name='edit_menu_category'),
    path('edit_item/<int:item_id>/', views.edit_menu_item, name='edit_menu_item'),
    path('', views.menu_category_list, name='menu_category_list'), 
]