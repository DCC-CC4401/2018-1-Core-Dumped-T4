from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from articlesApp.models import Article
from loansApp.models import Loan
from django.db import models
from datetime import datetime, timedelta

import random, os
import pytz
from django.contrib import messages

@login_required
def loan_data(request, loan_id):
    try:
        loan_bacan = Loan.objects.get(id=loan_id)
        article=loan_bacan.article

        last_loans = Loan.objects.filter(article=article,
                                         ending_date_time__lt=datetime.now(tz=pytz.utc)
                                         ).order_by('-ending_date_time')[:10]

        loan_list = list()
        for loan in last_loans:

            starting_day = loan.starting_date_time.strftime("%d-%m-%Y")
            ending_day = loan.ending_date_time.strftime("%d-%m-%Y")
            starting_hour = loan.starting_date_time.strftime("%H:%M")
            ending_hour = loan.ending_date_time.strftime("%H:%M")

            if starting_day == ending_day:
                loan_list.append(starting_day+" "+starting_hour+" a "+ending_hour)
            else:
                loan_list.append(starting_day + ", " + starting_hour + " a " +ending_day + ", " +ending_hour)


        context = {
            'user':loan_bacan.user,
            'loan':loan_bacan,
            'article': article,
            'last_loans': loan_list
        }

        return render(request, 'loan_data.html', context)
    except Exception as e:
        print(e)
        return redirect('/')
# Create your views here.
