from django.urls import path
from . import views

app_name = 'stocks'

urlpatterns = [
    path('', views.home, name='home'),
    path('stock/<str:symbol>/', views.stock_detail, name='stock_detail'),
]