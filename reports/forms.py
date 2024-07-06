from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput
from .models import Report
from guests.models import Guest


# Form for adding guests
class AddReport(forms.ModelForm):
    """

    Args:
        forms (_type_): _description_

    Returns:
        _type_: _description_
    """

    guests = forms.ModelMultipleChoiceField(
        queryset=Guest.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={"class": "guest-check-list"}),
        label="Guests to mention in the report",
        required=False
    )

    class Meta:
        model = Report
        fields = (
            "report_date",
            "report_text",
            "guests",
        )
        labels = {
            "report_date": "Select date",
            "report_text": "Keep your report short and sweet",
        }

        widgets = {
            "report_date": DatePickerInput(attrs={"class": "form-control"}),
            "report_text": forms.Textarea(attrs={"class": "form-control"}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['guests'].label_from_instance = self.label_from_instance

    def label_from_instance(self, obj):
        name_addon = f" ({obj.name_addon})" if obj.name_addon else ""
        last_name = f"{obj.last_name}" if obj.last_name else ""
        return f"{obj.first_name} {name_addon} {last_name}"