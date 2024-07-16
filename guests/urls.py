from django.urls import path
from .views.guests_list_views import guests_list_view, guests_list_all_view
from .views.guest_details_views import guest_details_view
from .views.add_guests_views import add_guest_view, update_guest_view

urlpatterns = [
    path('', guests_list_view, name='home'),
    path('guests/', guests_list_view, name='guests_list_temp'),
    path('guests/all/', guests_list_all_view, name='guests_list_all_temp'),
    path('guests/add_guest/', add_guest_view, name='add_guest_temp'),
    path('guests/update_guest/<int:id>', update_guest_view, name='update_guest_temp'),
    path('guests/<slug:slug>/', guest_details_view, name='guest_details_temp'),
]