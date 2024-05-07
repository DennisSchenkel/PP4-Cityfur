from . import views
from django.urls import path

urlpatterns = [
    path('', views.reports_list, name='home'),
    path('reports/', views.reports_list, name='reports_list'),
]