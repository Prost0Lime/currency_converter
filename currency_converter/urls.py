from django.urls import path
from . import views

urlpatterns = [
    path('api/rates/', views.currency_converter, name='currency_converter'),
]