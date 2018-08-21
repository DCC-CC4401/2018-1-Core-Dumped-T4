from django.shortcuts import render, redirect
from django.utils.timezone import localtime
import datetime
from articlesApp.models import Article
from django.contrib import messages
from reservationsApp.models import Reservation
from django.contrib.auth.decorators import login_required

from spacesApp.models import Space
from spacesApp.views import verificar_horario_habil

from reservationsApp.forms import ReservationForm


@login_required
def landing_articles(request):
    context = {}
    return render(request, 'articulos.html', context)


@login_required
def landing_spaces(request, date=None, filter=None):
    if date:
        current_date = date
        current_week = datetime.datetime.strptime(current_date, "%Y-%m-%d").date().isocalendar()[1]
    else:
        try:
            current_week = datetime.datetime.strptime(request.GET["date"], "%Y-%m-%d").date().isocalendar()[1]
            current_date = request.GET["date"]
        except:
            current_week = datetime.date.today().isocalendar()[1]
            current_date = datetime.date.today().strftime("%Y-%m-%d")

    if request.method == 'POST':
        filter_calendar = request.POST['espacios']
    elif filter is not None:
        filter_calendar = filter
    else:
        filter_calendar = "A"

    if filter_calendar == "A":
        reservations = Reservation.objects.filter(starting_date_time__week=current_week, state__in=['P', 'A'])
    else:
        reservations = Reservation.objects.filter(starting_date_time__week=current_week, state__in=['P', 'A'],
                                                  space__name=filter_calendar)

    colores = {'A': 'rgba(0,153,0,0.7)',
               'P': 'rgba(51,51,204,0.7)'}
    spaces = Space.objects.all()

    res_list = []
    for i in range(5):
        res_list.append(list())
    for r in reservations:
        reserv = []
        reserv.append(r.space.name)
        reserv.append(r.space.id)
        reserv.append(localtime(r.starting_date_time).strftime("%H:%M"))
        reserv.append(localtime(r.ending_date_time).strftime("%H:%M"))
        reserv.append(colores[r.state])
        res_list[r.starting_date_time.isocalendar()[2] - 1].append(reserv)

    move_controls = list()
    move_controls.append(
        (datetime.datetime.strptime(current_date, "%Y-%m-%d") + datetime.timedelta(weeks=-4)).strftime("%Y-%m-%d"))
    move_controls.append(
        (datetime.datetime.strptime(current_date, "%Y-%m-%d") + datetime.timedelta(weeks=-1)).strftime("%Y-%m-%d"))
    move_controls.append(
        (datetime.datetime.strptime(current_date, "%Y-%m-%d") + datetime.timedelta(weeks=1)).strftime("%Y-%m-%d"))
    move_controls.append(
        (datetime.datetime.strptime(current_date, "%Y-%m-%d") + datetime.timedelta(weeks=4)).strftime("%Y-%m-%d"))

    delta = (datetime.datetime.strptime(current_date, "%Y-%m-%d").isocalendar()[2]) - 1
    monday = (
        (datetime.datetime.strptime(current_date, "%Y-%m-%d") - datetime.timedelta(days=delta)).strftime("%d/%m/%Y"))

    form = ReservationForm()
    context = {'reservations': res_list,
               'current_date': current_date,
               'controls': move_controls,
               'actual_monday': monday,
               'spaces': spaces,
               'filter_calendar': filter_calendar,
               'form': form}
    return render(request, 'espacios.html', context)


@login_required
def landing_search(request, products):
    if not products:
        return landing_articles(request)
    else:
        context = {'productos': products,
                   'colores': {'D': '#009900',
                               'R': '#ffcc00',
                               'P': '#3333cc',
                               'L': '#cc0000'}
                   }
        return render(request, 'articulos.html', context)


@login_required
def search(request):
    if request.method == "GET":
        query = request.GET['query']
        # a_type = "comportamiento_no_definido"
        a_state = "A" if (request.GET['estado'] == "A") else request.GET['estado']

        if not (a_state == "A"):
            articles = Article.objects.filter(state=a_state, name__icontains=query.lower())
        else:
            articles = Article.objects.filter(name__icontains=query.lower())

        products = None if (request.GET['query'] == "") else articles
        return landing_search(request, products)


@login_required
def landing_page(request):
    user = request.user
    if not (user.is_superuser and user.is_staff):
        return redirect('landing_articles')
    return redirect('landing-panel')


@login_required
def crear_reserva1(request):
    print('Hola jejej')
    if request.method == 'POST':
        if request.user.enabled:
            try:
                space = Space.objects.get(id=request.POST['nombreEspacio'])
                string_inicio = request.POST['fecha_inicio'] + " " + request.POST['hora_inicio']
                print(string_inicio)
                start_date_time = datetime.datetime.strptime(string_inicio, '%Y-%m-%d %H:%M')
                string_fin = request.POST['fecha_fin'] + " " + request.POST['hora_fin']
                print(string_fin)
                end_date_time = datetime.datetime.strptime(string_fin, '%Y-%m-%d %H:%M')

                if start_date_time > end_date_time:
                    messages.warning(request, 'La reserva debe terminar después de iniciar.')
                elif start_date_time < datetime.datetime.now() + datetime.timedelta(hours=1):
                    messages.warning(request, 'Los pedidos deben ser hechos al menos con una hora de anticipación.')
                elif start_date_time.date() != end_date_time.date():
                    messages.warning(request, 'Los pedidos deben ser devueltos el mismo día que se entregan.')
                elif not verificar_horario_habil(start_date_time) and not verificar_horario_habil(end_date_time):
                    messages.warning(request, 'Los pedidos deben ser hechos en horario hábil.')
                else:
                    res = Reservation(space=space, starting_date_time=start_date_time,
                                      ending_date_time=end_date_time,
                                      user=request.user)
                    res.save()
                    print(space)
                    messages.success(request, 'Pedido realizado con éxito')
            except Exception as e:
                messages.warning(request, 'Ingrese una fecha y hora válida.')
        else:
            messages.warning(request, 'Usuario no habilitado para pedir préstamos')

        return redirect('landing_spaces')
