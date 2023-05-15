from django.shortcuts import render
from django.views import generic

# Create your views here.


def displayPage(request):
    return render(request, 'booking/booking.html')