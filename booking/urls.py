from django.urls import path
from . import views
from booking.views import (
    BookingList, BookingDetail, create_booking, 
    delete_booking, edit_booking, index
)

urlpatterns = [
    path('bookings/', BookingList.as_view(), name='booking_list'),
    path('bookings/create/', create_booking, name='booking_form'),
    path('bookings/<int:pk>/', BookingDetail.as_view(), name='booking_detail'),
    path(
        'delete_booking/<int:booking_id>/',
        delete_booking,
        name='delete_booking'
    ),
    path(
        'edit_booking/<int:booking_id>/',
        edit_booking,
        name='edit_booking'
    ),
    path('', index, name='home'),
]
