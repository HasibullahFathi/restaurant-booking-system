from django import forms
from .models import Booking, Table, Shift


class BookingForm(forms.ModelForm):
    shift = forms.ModelChoiceField(queryset=Shift.objects.all(), empty_label="Select a Shift")

    booking_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label="Booking Time")

    class Meta:
        model = Booking
        fields = ['table', 'shift', 'booking_date', 'phone_number', 'booking_time', 'number_of_guests', 'remarks']

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        # Filter available tables only
        self.fields['table'].queryset = Table.objects.filter(status='available')
