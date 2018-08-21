from django.forms import ModelForm
# Models
from .models import Reservation

class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['space', 'starting_date_time', 'ending_date_time']
