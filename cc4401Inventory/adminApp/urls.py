from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_panel, name="landing-panel"),
    path('user-panel/', views.user_panel, name="user-panel"),
    path('items-panel/', views.items_panel, name="items-panel"),
    path('items-panel/new-article', views.new_article, name="new-article"),
    path('items-panel/delete-article', views.delete_article, name="delete-article"),
    path('actions-panel/', views.actions_panel, name="actions-panel"),
    path('actions-panel/modify', views.modify_reservations, name="modify_reservations"),
    path('actions-panel/receive-loans', views.received_loans, name="received_loans"),
    path('actions-panel/lost-loans', views.lost_loans, name="lost_loans")
]