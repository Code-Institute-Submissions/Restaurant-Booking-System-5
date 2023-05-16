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
            if Booking.objects.filter(day=day, time=time).exists():
                error_message = "The selected time slot is already booked."
                messages.error(request, error_message)
                return redirect('booking_page')
            
            # Create a new booking 
            booking = Booking(user=request.user, day=day, time=time)
            booking.save()
            
            # Display a success message
            success_message = "Booking successful! Your slot has been reserved."
            messages.success(request, success_message)
            
            # Redirect to a success page or display a success message
            return redirect('booking_success')
    else:
        form = BookingForm()

    return render(request, 'booking/booking.html', {'form': form})