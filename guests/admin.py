from django.contrib import admin
from .models import Customer, Guest  # Import of the models Customers and Guests from the models.py file
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Guest)
class GuestAdmin(SummernoteModelAdmin):

    list_display = ('first_name', 'name_addon', 'gender')
    search_fields = ['first_name']
    list_filter = ('gender',)


@admin.register(Customer)
class CustomerAdmin(SummernoteModelAdmin):

    list_display = ('last_name', 'first_name')
    search_fields = ['first_name', 'last_name', 'guests__first_name']
    ### Add search_field for dog name