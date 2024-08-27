from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from.models import Booking, Profile, Shift, Table
from django.contrib import messages
from.forms import BookingForm
from django.http import Http404
from django.utils import timezone
from datetime import datetime, time


# Create your views here.

class BookingList(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking/booking.html'
    context_object_name = 'bookings'
    paginate_by = 8

    def get_queryset(self):
        try:
            profile = Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            raise Http404("Profile does not exist for the user.")

        if profile.role == 1:
            return Booking.objects.all().order_by("-created_on")
        else:
            return Booking.objects.filter(user=self.request.user).order_by("-created_on")

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().get(request, *args, **kwargs)

class BookingDetail(DetailView):
    model = Booking
    template_name = 'booking/booking_detail.html'
    context_object_name = 'booking' 

def index(request):
    return render(request, 'booking/index.html')




@login_required
def create_booking(request):
    tables = Table.objects.all()

    form = BookingForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user

            selected_shift = booking.shift
            booking_time = booking.booking_time

            if booking.booking_date < timezone.now().date():
                messages.error(request, "Booking date must be in the future.")
                return render(request, 'booking/booking_form.html', {'form': form, 'tables': tables})

            if not (selected_shift.start_time <= booking_time <= selected_shift.end_time):
                messages.error(request, f"Booking time must be between {selected_shift.start_time} and {selected_shift.end_time} for the {selected_shift.name} shift.")
                return render(request, 'booking/booking_form.html', {'form': form, 'tables': tables})

            duplicate_booking = Booking.objects.filter(
                table=booking.table,
                booking_date=booking.booking_date,
                shift=booking.shift,
                status=2 
            ).exclude(id=booking.id).exists()

            if duplicate_booking:
                messages.error(request, "This table is already booked at the selected time during the shift.")
                return render(request, 'booking/booking_form.html', {'form': form, 'tables': tables})

            booking.save()
            booking.table.status = '2' 
            booking.table.save()

            messages.success(request, "Your booking has been successfully created!")
            return redirect('booking_list')

        else:
            print("Form Errors:", form.errors)
            messages.error(request, "There was an error with your booking.")

    return render(request, 'booking/booking_form.html', {'form': form, 'tables': tables})



@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    tables = Table.objects.all()

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        
        if form.is_valid():
            updated_booking = form.save(commit=False)
            updated_booking.user = request.user

            selected_shift = updated_booking.shift
            booking_time = updated_booking.booking_time

            if updated_booking.booking_date < timezone.now().date():
                messages.error(request, "Booking date must be in the future.")
                return render(request, 'booking/booking_form.html', {'form': form, 'tables': tables})

            if not (selected_shift.start_time <= booking_time <= selected_shift.end_time):
                messages.error(request, f"Booking time must be between {selected_shift.start_time} and {selected_shift.end_time} for the {selected_shift.name} shift.")
                return render(request, 'booking/booking_form.html', {'form': form, 'tables': tables})

            if booking.table != updated_booking.table:
                booking.table.status = 1
                booking.table.save()

                if Booking.objects.filter(
                    table=updated_booking.table,
                    booking_date=updated_booking.booking_date,
                    shift=updated_booking.shift,
                    status=2
                ).exists():
                    messages.error(request, "This table is already booked at the selected time during the shift.")
                    return render(request, 'booking/booking_form.html', {'form': form, 'tables': tables})

                updated_booking.table.status = '2' 
                updated_booking.table.save()

            updated_booking.save()

            messages.success(request, "Your booking has been successfully updated!")
            return redirect('booking_list')

        else:
            messages.error(request, "There was an error with your booking.")
    
    else:
        form = BookingForm(instance=booking)

    return render(request, 'booking/booking_form.html', {'form': form, 'tables': tables})




@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    table = booking.table
    table.status = 1
    table.save()

    booking.delete()

    messages.success(request, "The booking has been successfully deleted.")
    return redirect('booking_list')