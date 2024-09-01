from django import forms
from django.db import models
from .models import Booking, Table, Shift


class BookingForm(forms.ModelForm):
    shift = forms.ModelChoiceField(
        queryset=Shift.objects.all(),
        empty_label="Select a Shift"
    )
    booking_time = forms.TimeField(
        widget=forms.TimeInput(
            format='%H:%M',
            attrs={'type': 'time'}
        ),
        label="Booking Time"
    )
    booking_date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'}),
        label="Booking Date"
    )
    number_of_guests = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': '1'}),
        label="Number of Guests"
    )

    class Meta:
        model = Booking
        fields = [
            'table', 'shift', 'booking_date', 'phone_number',
            'booking_time', 'number_of_guests', 'remarks'
        ]

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)

        if instance and instance.pk:
            current_table = instance.table
            self.fields['table'].queryset = Table.objects.filter(
                models.Q(status=1) | models.Q(id=current_table.id)
            )
        else:
            self.fields['table'].queryset = Table.objects.filter(status=1)

    def clean_number_of_guests(self):
        number_of_guests = self.cleaned_data.get('number_of_guests')
        if number_of_guests < 1:
            raise forms.ValidationError(
                "Number of guests cannot be negative or zero."
            )
        return number_of_guests
