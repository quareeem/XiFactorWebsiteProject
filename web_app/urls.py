from . import views
from django.urls import path
from django.conf.locale import LANG_INFO

urlpatterns = [
    path('', views.home, name="home"),
    path('e/', views.e, name="e"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('sector/', views.sector, name="sector"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('contacts/', views.contacts, name="contacts"),
    path('solutions/', views.solutions, name="solutions"),
    path('solutions/arxiv', views.solutions_arxiv, name="solutions_arxiv"),
    path('solutions/sebes', views.solutions_sebes, name="solutions_sebes"),
    path('research/', views.research, name="research"),
    path('success/', views.success, name="success"),
]
