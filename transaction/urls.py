from django.urls import path

from transaction import views

urlpatterns = [
    path('transaction/', views.transaction, name='transaction'),
    path('transaction/send/', views.send, name='send'),
    path('transaction/withdraw/', views.withdraw, name='withdraw'),
    path('transaction/getHistory/', views.get_history, name='get_history'),
    path('transaction/<str:card_number>/history/', views.history, name='history'),
]
