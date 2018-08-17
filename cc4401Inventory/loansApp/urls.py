from django.urls import path

from . import views

urlpatterns = [
    path('change/', views.change, name='change'),
    path('<int:loan_id>', views.loan_data, name='loan_data'),
]