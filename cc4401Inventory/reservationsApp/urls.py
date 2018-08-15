from django.urls import path
from . import views

urlpatterns = [
    path('<int:reservation_id>', views.reservation_data, name='reseravtion_data'),
    path('delete/', views.delete, name='delete_reservation'),
]
