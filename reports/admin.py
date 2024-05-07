from django.contrib import admin
from .models import Reports  # Import of the models Reports from the models.py file
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
admin.site.register(Reports)
