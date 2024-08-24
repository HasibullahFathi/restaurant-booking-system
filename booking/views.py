from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'booking/index.html')
    

def book_table(request):
    return render(request, 'booking/book_table.html')
    # if request.method == 'POST':
    #     table_number = request.POST.get('table_number')
    #     name = request.POST.get('name')
    #     date = request.POST.get('date')
    #     time = request.POST.get('time')
        
    #     # Save the booking details to the database
        
    #     return HttpResponse("Booking successful!")
    # else:
    #     return render(request, 'booking/book_table.html')