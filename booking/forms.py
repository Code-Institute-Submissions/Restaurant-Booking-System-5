from django import forms


class BookingForm(forms.Form):
    # Define your form fields here
    day = forms.CharField(max_length=10)
    time = forms.CharField(max_length=10)