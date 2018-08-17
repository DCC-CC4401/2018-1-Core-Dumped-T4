from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from articlesApp.models import Article
from loansApp.models import Loan


def change(request):
    if request.method=='POST':
        artid = request.POST.get('artid')
        loanid = request.POST.get('loanid')
        articulo = Article.objects.get(pk=artid)
        articulo.state = 'L'
        articulo.save()
        ruta = "/loans/"+str(loanid)
        return HttpResponseRedirect(ruta)
    else:
        return redirect('/')




@login_required
def loan_data(request, loan_id):
    try:
        loan_bacan = Loan.objects.get(id=loan_id)
        article = loan_bacan.article
        currentuser = request.user

        context = {
            'usuario':loan_bacan.user,
            'loan':loan_bacan,
            'article': article,
            'currentuser':currentuser,
        }

        return render(request, 'loan_data.html', context)
    except Exception as e:
        print(e)
        return redirect('/')

# Create your views here.
