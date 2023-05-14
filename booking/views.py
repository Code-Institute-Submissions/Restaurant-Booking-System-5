from django.shortcuts import render

# Create your views here.
def displayPage(request):
    return render(request, 'booking/booking.html')