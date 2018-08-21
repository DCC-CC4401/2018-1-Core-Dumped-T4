from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('articles/', views.landing_articles, name='landing_articles'),
    path('spaces/', views.landing_spaces, name='landing_spaces'),
    path('spaces/<str:date>/<str:filter>', views.landing_spaces, name='landing_spaces'),
    path('search/', views.search, name='search'),
]
