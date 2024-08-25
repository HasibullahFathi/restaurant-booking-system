from django import forms
from .models import Booking
from django.contrib.auth import get_user_model
from .models import Profile

class BookingForm(forms.ModelForm):
    # Additional fields
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)

    class Meta:
        model = Booking
        fields = ('name', 'email', 'phone', 'table', 'booking_date', 'booking_time', 'number_of_guests', 'remarks')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            try:
                profile = Profile.objects.get(user=user)
                self.fields['name'].initial = user.get_full_name()
                self.fields['email'].initial = user.email
                self.fields['phone'].initial = profile.phone_number
            except Profile.DoesNotExist:
                self.fields['name'].initial = user.get_full_name()
                self.fields['email'].initial = user.email
                self.fields['phone'].initial = ''
