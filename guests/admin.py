from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import (
    Customer,
    Guest,
    Presence,
)  # Import of the models Customers and Guests from the models.py file


@admin.register(Customer)
class CustomerAdmin(SummernoteModelAdmin):
    """
    Admin class for managing customers.

    Args:
        SummernoteModelAdmin: Base admin class for models with
            Summernote fields.

    Attributes:
        list_display (tuple): A tuple of field names to be displayed
            in the admin list view.
        search_fields (list): A list of field names to be used
            for searching in the admin list view.
    """
    list_display = ("last_name", "first_name", "id")
    search_fields = ["first_name", "last_name", "guests__first_name"]


@admin.register(Guest)
class GuestAdmin(SummernoteModelAdmin):
    """
    Admin class for managing guests.

    This class extends the SummernoteModelAdmin class and provides additional
        functionality for managing guests in the admin interface.

    Attributes:
        list_display (tuple): A tuple of field names
            to be displayed in the admin list view.
        search_fields (list): A list of field names
            to be used for searching guests in the admin interface.
        list_filter (tuple): A tuple of field names
            to be used for filtering guests in the admin interface.
    """

    list_display = ("first_name", "name_addon", "gender", "id")
    search_fields = ["first_name"]
    list_filter = ("gender",)


@admin.register(Presence)
class GuestPresence(SummernoteModelAdmin):
    """
    Admin class for managing guest presence.

    This class extends the SummernoteModelAdmin class and provides additional
        functionality for managing guest presence in the admin interface.

    Attributes:
        list_display (tuple): A tuple of field names
            to be displayed in the admin list view.
        search_fields (list): A list of field names
            to be used for searching guest presence in the admin interface.
        list_filter (tuple): A tuple of field names
            to be used for filtering guest presence in the admin interface.
    """

    list_display = ("date", "guest", "check_in", "check_out", "id")
    search_fields = ["guest", "date"]
    list_filter = ("date",)
