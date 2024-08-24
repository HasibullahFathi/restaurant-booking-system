from . import views
from django.urls import path
from booking.views import BookingList

urlpatterns = [
    path('', views.index, name='home'),
    path('mybooking/', views.book_table, name='book_table'),
    path('bookings/', BookingList.as_view(), name='booking_list'),

]