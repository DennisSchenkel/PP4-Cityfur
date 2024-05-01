from . import views
from django.urls import path

urlpatterns = [
    path('', views.guests_list, name='home'),
    path('guests/', views.guests_list, name='guests_list'),
    path('guests/<slug:slug>/', views.guest_details, name='guest_details'),
]