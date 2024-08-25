from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from.models import Booking, Profile
from django.contrib import messages
from.forms import BookingForm
from django.http import Http404

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
    template_name = 'booking/booking_detail.html'  # The template to render
    context_object_name = 'booking'  # The context variable for the template

def index(request):
    return render(request, 'booking/index.html')
    

@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Automatically assign the logged-in user
            booking.save()
            messages.success(request, "Your booking has been successfully created!")
            return redirect('booking_list')  # Redirect to your booking list or a success page
        else:
            messages.error(request, "There was an error with your booking.")
    else:
        form = BookingForm()

    return render(request, 'booking/booking_form.html', {'form': form})

