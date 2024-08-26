from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from.models import Booking, Profile, Shift
from django.contrib import messages
from.forms import BookingForm
from django.http import Http404
from django.utils import timezone
from datetime import datetime, time


# Create your views here.

class BookingList(LoginRequiredMixin, ListView):
    queryset = Booking.objects.all().order_by("-created_on")
    template_name = 'booking/booking.html'
    context_object_name = 'bookings'  # This sets the name of the context variable
    paginate_by = 8

    def get_queryset(self):
        try:
            profile = Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            raise Http404("Profile does not exist for the user.")

        if profile.role == 1:  # Admin role
            return Booking.objects.all()
        else:  # Regular user (Customer)
            return Booking.objects.filter(user=self.request.user)

class BookingDetail(DetailView):
    model = Booking
    template_name = 'booking/booking_detail.html'
    context_object_name = 'booking' 

def index(request):
    return render(request, 'booking/index.html')

@login_required
def create_booking(request, booking_id=None):
    if booking_id:

        booking = get_object_or_404(Booking, id=booking_id)
        form = BookingForm(request.POST or None, instance=booking)
    else:

        form = BookingForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user

            # Get the selected shift
            selected_shift = booking.shift

            # Validate that the booking time falls within the shift time
            if not (selected_shift.start_time <= booking.booking_time <= selected_shift.end_time):
                messages.add_message(request, messages.ERROR, f"Booking time must be between {selected_shift.start_time} and {selected_shift.end_time} for the {selected_shift.name}.")
                return render(request, 'booking/booking_form.html', {'form': form})

            # Check if the table is available for the selected date, shift, and time
            if Booking.objects.filter(
                    table=booking.table, 
                    booking_date=booking.booking_date, 
                    shift=booking.shift,
                    booking_time=booking.booking_time, 
                    status=1).exclude(id=booking.id).exists():
                messages.error(request, "This table is already booked at the selected time during the shift.")

                return render(request, 'booking/booking_form.html', {'form': form})

            # Save the booking and update the table status
            booking.save()
            booking.table.status = 'reserved'
            booking.table.save()

            messages.add_message(request, messages.SUCCESS, "Your booking has been successfully created/updated!")
            return redirect('booking_list')
        else:
            messages.add_message(request, messages.ERROR, "There was an error with your booking.")
    else:
        if booking_id:
            form = BookingForm(instance=booking)


    return render(request, 'booking/booking_form.html', {'form': form})

    



