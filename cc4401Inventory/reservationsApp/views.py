from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from reservationsApp.models import Reservation
from django.contrib import messages


def delete(request):
    if request.method == 'POST':
        reservation_ids = request.POST.getlist('reservation')
        try:
            for reservation_id in reservation_ids:
                reservation = Reservation.objects.get(id=reservation_id)
                if reservation.state == 'P':
                    reservation.delete()
        except:
            messages.warning(request, 'Ha ocurrido un error y la reserva no se ha eliminado')

        return redirect('user_data', user_id=request.user.id)


@login_required
def reservation_data(request, reservation_id):
    try:
        reservation_bacan = Reservation.objects.get(id=reservation_id)
        space = reservation_bacan.space
        currentuser = request.user


        context = {
            'usuario': reservation_bacan.user,
            'reservation': reservation_bacan,
            'space': space,
            'currentuser': currentuser,
            }

        return render(request, 'reservation_data.html', context)
    except Exception as e:
        print(e)
        return redirect('/')
