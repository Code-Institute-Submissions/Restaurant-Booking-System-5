from django.shortcuts import render, redirect
from django.views import generic
from .models import Slot, Booking
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookingForm

# Create your views here.


def displayPage(request):
    return render(request, 'booking/booking.html')

@login_required
def book_slot(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            slot = form.cleaned_data['slot']
            day = slot.day
            time = slot.time
            
            # Check if time slot is already booked
            if Booking.objects.filter(slot=slot).exists():
                error_message = "The selected time slot is already booked."
                return render(request, 'booking/booking.html', {'form': form, 'error_message': error_message})
            
            # Create a new booking 
            booking = Booking(user=request.user, slot=slot)
            booking.save()
            
            # Redirect to a success page or display a success message
            return redirect('booking_success')
    else:
        form = BookingForm()

    return render(request, 'booking/booking.html', {'form': form})