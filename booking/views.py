from django.shortcuts import render, redirect
from django.views import generic
from .models import Slot, Booking
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookingForm
from django.contrib import messages

# Create your views here.


def displayPage(request):
    return render(request, 'booking/booking.html')


@login_required
def book_slot(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            day = form.cleaned_data['day']
            time = form.cleaned_data['time']

            # Check if time slot is already booked
            if Booking.objects.filter(slot__day=day, slot__time=time).exists():
                error_message = "The selected time slot is already booked."
                messages.error(request, error_message)
            else:
                # Create a new booking
                slot = Slot.objects.get(day=day, time=time)
                booking = Booking(user=request.user, slot=slot)
                booking.save()
                success_message = "Booking successful!"
                messages.success(request, success_message)
        else:
            error_message = "Invalid form submission."
            messages.error(request, error_message)
    else:
        form = BookingForm()

    return redirect('booking')