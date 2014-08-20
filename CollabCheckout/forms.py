from django import forms
from CollabCheckout.models import RoomSlot

__author__ = 'Alex Clement'

class RoomSlotForm(forms.ModelForm):

    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Date', 'id':'datepicker'}))
    period = forms.ChoiceField(widget=forms.TextInput(attrs={'id':'PeriodsName'}))
    room = forms.ChoiceField(widget=forms.TextInput(attrs={'id':'RoomsName'}))


    class Meta:
        model = RoomSlot
        fields = ('email', 'date', 'period', 'room')