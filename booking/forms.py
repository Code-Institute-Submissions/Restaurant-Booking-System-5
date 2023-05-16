from django import forms
from .models import Slot


class BookingForm(forms.Form):
    slot = forms.ModelChoiceField(queryset=Slot.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slot'].widget.attrs.update({'class': 'form-control'})