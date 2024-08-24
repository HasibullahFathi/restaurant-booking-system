from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('booking/', views.book_table, name='book_table'),

]