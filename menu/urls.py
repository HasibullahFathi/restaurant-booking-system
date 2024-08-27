from . import views
from django.urls import path
from booking.views import BookingList, BookingDetail, create_booking

urlpatterns = [

    path('', views.menu_category_list, name='menu_category_list')
]