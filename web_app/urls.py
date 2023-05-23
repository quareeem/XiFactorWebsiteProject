from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('e/', views.e, name="e"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('sector/', views.sector, name="sector"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('contacts/', views.contacts, name="contacts"),
    path('success/', views.success, name="success"),
]
