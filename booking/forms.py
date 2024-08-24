from .models import Booking
from django import forms



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'email', 'phone', 'table', 'booking_date', 'booking_time', 'number_of_guest', 'remarks')