from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from reservationsApp.models import Reservation
from loansApp.models import Loan
from articlesApp.models import Article
<<<<<<< HEAD
from articlesApp.forms import ArticleForm
=======
>>>>>>> 8d5f0dc9c7d71c4df133d1bb2eb024bcb21c9d21
from spacesApp.models import Space
from mainApp.models import User
from datetime import datetime, timedelta, date
import pytz
from django.utils.timezone import localtime

<<<<<<< HEAD

=======
>>>>>>> 8d5f0dc9c7d71c4df133d1bb2eb024bcb21c9d21
@login_required
def user_panel(request):
    user = request.user
    if not (user.is_superuser and user.is_staff):
        return redirect('/')
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'user_panel.html', context)

<<<<<<< HEAD

=======
>>>>>>> 8d5f0dc9c7d71c4df133d1bb2eb024bcb21c9d21
@login_required
def items_panel(request):
    user = request.user
    if not (user.is_superuser and user.is_staff):
        return redirect('/')
    articles = Article.objects.all()
    spaces = Space.objects.all()
<<<<<<< HEAD
    form = ArticleForm()
    context = {
        'articles': articles,
        'spaces': spaces,
        'form': form,
    }
    return render(request, 'items_panel.html', context)


=======
    context = {
        'articles': articles,
        'spaces': spaces
    }
    return render(request, 'items_panel.html', context)

>>>>>>> 8d5f0dc9c7d71c4df133d1bb2eb024bcb21c9d21
@login_required
def actions_panel(request):
    user = request.user
    if not (user.is_superuser and user.is_staff):
        return redirect('/')
    try:
        current_week = datetime.strptime(request.GET["date"], "%Y-%m-%d").date().isocalendar()[1]
        current_date = request.GET["date"]
    except:
        current_date = date.today().strftime("%Y-%m-%d")
        current_week = date.today().isocalendar()[1]

    colores = {'A': 'rgba(0,153,0,0.7)',
               'P': 'rgba(51,51,204,0.7)',
<<<<<<< HEAD
               'R': 'rgba(153, 0, 0,0.7)'}
=======
                'R': 'rgba(153, 0, 0,0.7)'}
>>>>>>> 8d5f0dc9c7d71c4df133d1bb2eb024bcb21c9d21

    reservations = Reservation.objects.filter(state='P').order_by('starting_date_time')
    current_week_reservations = Reservation.objects.filter(starting_date_time__week = current_week)
    actual_date = datetime.now(tz=pytz.utc)
    try:
        if request.method == "GET":
            if request.GET["filter"]=='vigentes':
                loans = Loan.objects.filter(ending_date_time__gt=actual_date).order_by('starting_date_time')
            elif request.GET["filter"]=='caducados':
                loans = Loan.objects.filter(ending_date_time__lt=actual_date, article__state='P').order_by('starting_date_time')
            elif request.GET["filter"]=='perdidos':
                loans = Loan.objects.filter(ending_date_time__lt=actual_date, article__state='L').order_by('starting_date_time')
            else:
                loans = Loan.objects.all().order_by('starting_date_time')
    except:
        loans = Loan.objects.all().order_by('starting_date_time')

    res_list = []
    for i in range(5):
        res_list.append(list())
    for r in current_week_reservations:
        reserv = list()
        reserv.append(r.space.name)
        reserv.append(localtime(r.starting_date_time).strftime("%H:%M"))
        reserv.append(localtime(r.ending_date_time).strftime("%H:%M"))
        reserv.append(colores[r.state])
        res_list[r.starting_date_time.isocalendar()[2] - 1].append(reserv)

    move_controls = list()
    move_controls.append(
        (datetime.strptime(current_date, "%Y-%m-%d") + timedelta(weeks=-4)).strftime("%Y-%m-%d"))
    move_controls.append(
        (datetime.strptime(current_date, "%Y-%m-%d") + timedelta(weeks=-1)).strftime("%Y-%m-%d"))
    move_controls.append(
        (datetime.strptime(current_date, "%Y-%m-%d") + timedelta(weeks=1)).strftime("%Y-%m-%d"))
    move_controls.append(
        (datetime.strptime(current_date, "%Y-%m-%d") + timedelta(weeks=4)).strftime("%Y-%m-%d"))

    delta = (datetime.strptime(current_date, "%Y-%m-%d").isocalendar()[2]) - 1
    monday = (
        (datetime.strptime(current_date, "%Y-%m-%d") - timedelta(days=delta)).strftime("%d/%m/%Y"))

<<<<<<< HEAD
=======

>>>>>>> 8d5f0dc9c7d71c4df133d1bb2eb024bcb21c9d21
    context = {
        'reservations_query': reservations,
        'loans': loans,
        'reservations': res_list,
        'current_date': current_date,
        'controls': move_controls,
        'actual_monday': monday
    }
    return render(request, 'actions_panel.html', context)


def modify_reservations(request):
    user = request.user
    if not (user.is_superuser and user.is_staff):
        return redirect('/')
    if request.method == "POST":

        accept = True if (request.POST["accept"] == "1") else False
<<<<<<< HEAD
        reservations = Reservation.objects.filter(id__in=request.POST.getlist("selected"))
=======
        reservations = Reservation.objects.filter(id__in=request.POST["selected"])
>>>>>>> 8d5f0dc9c7d71c4df133d1bb2eb024bcb21c9d21
        if accept:
            for reservation in reservations:
                reservation.state = 'A'
                reservation.save()
        else:
            for reservation in reservations:
                reservation.state = 'R'
                reservation.save()

<<<<<<< HEAD
    return redirect('actions-panel')


@login_required
def lost_loans(request):
    user = request.user
    if not (user.is_superuser and user.is_staff):
        return redirect('/')
    if request.method == "POST":
        loans = Loan.objects.filter(id__in=request.POST.getlist("loans"))
        for loan in loans:
            loan.state = Loan.PERDIDO
            loan.save()
    return redirect('actions-panel')


@login_required
def received_loans(request):
    user = request.user
    if not (user.is_superuser and user.is_staff):
        return redirect('/')
    if request.method == "POST":
        loans = Loan.objects.filter(id__in=request.POST.getlist("loans"))
        for loan in loans:
            loan.state = Loan.RECIBIDO
            loan.save()
    return redirect('actions-panel')


@login_required
def new_article(request):
    user = request.user
    if not (user.is_superuser and user.is_staff):
        return redirect('/')
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('items-panel')


@login_required
def delete_article(request):
    user = request.user
    if not (user.is_superuser and user.is_staff):
        return redirect('/')
    if request.method == "POST":
        article = Article.objects.get(id=request.POST.get('article_id'))
        article.delete()
        return redirect('items-panel')
=======
    return redirect('/admin/actions-panel')
>>>>>>> 8d5f0dc9c7d71c4df133d1bb2eb024bcb21c9d21
