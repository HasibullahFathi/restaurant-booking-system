from django import forms
from django.db import models
from .models import Booking, Table, Shift


class BookingForm(forms.ModelForm):
    shift = forms.ModelChoiceField(queryset=Shift.objects.all(), empty_label="Select a Shift")

    booking_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label="Booking Time")

    class Meta:
        model = Booking
        fields = ['table', 'shift', 'booking_date', 'phone_number', 'booking_time', 'number_of_guests', 'remarks']

    def __init__(self, *args, **kwargs):
        # Ensure we correctly handle the instance
        instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)

        if instance and instance.pk:
            # Editing an existing booking
            current_table = instance.table
            self.fields['table'].queryset = Table.objects.filter(
                models.Q(status=1) | models.Q(id=current_table.id)
            )
        else:
            # Creating a new booking, only show available tables
            self.fields['table'].queryset = Table.objects.filter(status=1)