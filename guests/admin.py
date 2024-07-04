from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import (
    Customer,
    Guest,
    Presence,
)  # Import of the models Customers and Guests from the models.py file


@admin.register(Customer)
class CustomerAdmin(SummernoteModelAdmin):
    """_summary_

    Args:
        SummernoteModelAdmin (_type_): _description_
    """

    list_display = ("last_name", "first_name", "id")
    search_fields = ["first_name", "last_name", "guests__first_name"]
    ### Add search_field for dog name


@admin.register(Guest)
class GuestAdmin(SummernoteModelAdmin):
    """_summary_

    Args:
        SummernoteModelAdmin (_type_): _description_
    """

    list_display = ("first_name", "name_addon", "gender", "id")
    search_fields = ["first_name"]
    list_filter = ("gender",)


@admin.register(Presence)
class GuestAdmin(SummernoteModelAdmin):
    """_summary_

    Args:
        SummernoteModelAdmin (_type_): _description_
    """

    list_display = ("date", "guest", "check_in", "check_out", "id")
    search_fields = ["guest", "date"]
    list_filter = ("date",)
