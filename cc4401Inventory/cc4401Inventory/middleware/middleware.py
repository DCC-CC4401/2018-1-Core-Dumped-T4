from django.utils import timezone
from reservationsApp.models import Reservation

class midUpdateQuincho(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        reservaciones = Reservation.objects.filter(space__name='quincho')
        if reservaciones:
            for r in reservaciones:
                if r.starting_date_time - timezone.timedelta(hours=24) <= timezone.now() and r.state == 'P':
                    r.state='R'
                    r.save()

        return self.get_response(request)