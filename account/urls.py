from django.urls import path

from account import views

urlpatterns = [
    path('accounts/', views.entry, name='entry'),
    path('accounts/<str:card_number>/summary/', views.summary, name='summary'),
]
