from . import views
from django.urls import path
from booking.views import BookingList, BookingDetail, create_booking

urlpatterns = [
    path('', views.index, name='home'),
    path('bookings/create/', views.create_booking, name='booking_form'),
    path('edit_booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('bookings/', BookingList.as_view(), name='booking_list'),
    path('bookings/<int:pk>/', BookingDetail.as_view(), name='booking_detail'),
    path('delete_booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
]