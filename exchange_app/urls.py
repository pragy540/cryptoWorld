from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('markets', views.markets, name="markets"),
    path('trade', views.trade, name="trade"),
    path('portfolio', views.portfolio, name="portfolio"),
    path('checkout', views.checkout, name="checkout"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('signup', views.signup, name="signup"),
    path('exchangeList', views.exchangeList, name="exchangeList"),
    path('credentialsAPI/<exchange_name>/', views.credentialsAPI, name="credentialsAPI"),
]
