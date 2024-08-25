from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.http import HttpResponse
from.models import Booking

# Create your views here.

class BookingList(ListView):
    queryset = Booking.objects.all().order_by("-created_on")
    template_name = 'booking/booking.html'
    context_object_name = 'bookings'  # This sets the name of the context variable
    paginate_by = 8

class BookingDetail(DetailView):
    model = Booking
    template_name = 'booking/booking_detail.html'  # The template to render
    context_object_name = 'booking'  # The context variable for the template

def index(request):
    return render(request, 'booking/index.html')
    

def book_table(request):
    return render(request, 'booking/book_table.html')