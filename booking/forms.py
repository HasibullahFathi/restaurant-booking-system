from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['table', 'booking_date', 'phone_number', 'booking_time', 'number_of_guests', 'remarks']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
