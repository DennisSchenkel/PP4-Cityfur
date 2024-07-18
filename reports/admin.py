from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Report


@admin.register(Report)
class CustomAdmin(SummernoteModelAdmin):

    list_display = ("report_date", "report_text", "created_on", "id")
