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
            slot = form.cleaned_data['slot']
                     
            if slot.booked:
                # Cancel the booking
                slot.booked = False
                slot.save()
                
                # Display a success message
                success_message = "Booking canceled successfully."
                messages.success(request, success_message)
            else:
               
                # Book the slot
                slot.booked = True
                slot.save()
                    
                # Display a success message
                success_message = "Booking successful! Your slot has been reserved."
                messages.success(request, success_message)

            return redirect('booking_page')
    else:
        form = BookingForm()

    return render(request, 'booking/booking.html', {'form': form})