from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Report


@admin.register(Report)
class CustomAdmin(SummernoteModelAdmin):
    """A custom admin class for managing reports.

    This class extends the SummernoteModelAdmin class to provide additional
        functionality for managing reports in the admin interface.

    Attributes:
        list_display (tuple): A tuple of field names to be
            displayed in the admin list view.

    """

    list_display = ("report_date", "report_text", "created_on", "id")
