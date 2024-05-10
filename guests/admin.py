from django.contrib import admin
from .models import Customer, Guest, Presence  # Import of the models Customers and Guests from the models.py file
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Customer)
class CustomerAdmin(SummernoteModelAdmin):

    list_display = ('last_name', 'first_name')
    search_fields = ['first_name', 'last_name', 'guests__first_name', 'id']
    ### Add search_field for dog name

@admin.register(Guest)
class GuestAdmin(SummernoteModelAdmin):

    list_display = ('first_name', 'name_addon', 'gender', 'id')
    search_fields = ['first_name']
    list_filter = ('gender',)

@admin.register(Presence)
class GuestAdmin(SummernoteModelAdmin):

    list_display = ('date', 'guest', 'check_in', 'check_out', 'id')
    search_fields = ['guest', 'date']
    list_filter = ('date',)



