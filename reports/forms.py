from django import forms
from django.utils.safestring import mark_safe
from bootstrap_datepicker_plus.widgets import TimePickerInput
from .models import Report


# Form for adding guests
class AddReport(forms.ModelForm):
    """

    Args:
        forms (_type_): _description_

    Returns:
        _type_: _description_
    """

    class Meta:
        model = Report
        fields = (
            "report_date",
            "report_text",
        )
        labels = {
            "report_date": "Date",
            "report_text": "Report",
        }

        widgets = {
            "report_date": forms.DateInput(attrs={"class": "form-control"}),
            "report_text": forms.TextInput(attrs={"class": "form-control"}),
        }

