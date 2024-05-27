from .views.guests_list_views import guests_list
from .views.guest_details_views import guest_details
from .views.add_guests_views import add_guest_form
from django.urls import path

urlpatterns = [
    path('', guests_list, name='home'),
    path('guests/', guests_list, name='guests_list'),
    path('guests/add_guest/', add_guest_form, name='add_guest'),
    path('guests/<slug:slug>/', guest_details, name='guest_details'),
]