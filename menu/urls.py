from . import views
from django.urls import path

urlpatterns = [

    path('', views.menu_category_list, name='menu_category_list'),
    path('create/', views.create_menu_and_category, name='create_menu'),
    
]