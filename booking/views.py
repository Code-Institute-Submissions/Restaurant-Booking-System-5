from django.shortcuts import render
from django.views import generic
from .models import Slot

# Create your views here.


def displayPage(request):
    return render(request, 'booking/booking.html')
