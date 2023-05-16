from django.shortcuts import render, redirect
from django.views import generic
from .models import Slot, Booking
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def displayPage(request):
    return render(request, 'booking/booking.html')

