from django import forms
from django.utils.safestring import mark_safe
from bootstrap_datepicker_plus.widgets import TimePickerInput, DatePickerInput
from .models import Guest, Presence


# Widget for displaying an image preview
class ImagePreviewWidget(forms.ClearableFileInput):
    """_summary_

    Args:
        forms (_type_): _description_
    """

    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and hasattr(value, "url"):
            output.append(
                f'<img src="{value.url}" width="200" height="200" style="object-fit: cover;"/>'
            )
        output.append(super().render(name, value, attrs, renderer))
        return mark_safe("".join(output))


# Form for adding guests
class AddGuest(forms.ModelForm):
    """

    Args:
        forms (_type_): _description_

    Returns:
        _type_: _description_
    """

    class Meta:
        model = Guest
        fields = (
            "first_name",
            "last_name",
            "name_addon",
            "gender",
            "image",
            "date_of_birth",
            "information",
            "food",
            "food_time_1",
            "food_time_2",
            "food_time_3",
            "medication",
            "medication_time_1",
            "medication_time_2",
            "medication_time_3",
            "customer_id",
        )
        labels = {
            "first_name": "First name",
            "last_name": "Last name",
            "name_addon": "Name addon",
            "gender": "Gender",
            "image": "Image",
            "date_of_birth": "Date of Birth",
            "information": "Information",
            "food": "Food",
            "food_time_1": "Food time 1",
            "food_time_2": "Food time 2",
            "food_time_3": "Food time 3",
            "medication": "Medication",
            "medication_time_1": "Medication time 1",
            "medication_time_2": "Medication time 2",
            "medication_time_3": "Medication time 3",
            "customer_id": "",
        }

        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "name_addon": forms.TextInput(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "image": ImagePreviewWidget(attrs={"class": "form-control"}),
            "date_of_birth": DatePickerInput(attrs={"class": "form-control"}),
            "information": forms.Textarea(attrs={"class": "form-control"}),
            "food": forms.SelectMultiple(attrs={"class": "form-control"}),
            "food_time_1": TimePickerInput(attrs={"class": "form-control"}),
            "food_time_2": TimePickerInput(attrs={"class": "form-control"}),
            "food_time_3": TimePickerInput(attrs={"class": "form-control"}),
            "medication": forms.SelectMultiple(attrs={"class": "form-control"}),
            "medication_time_1": TimePickerInput(attrs={"class": "form-control"}),
            "medication_time_2": TimePickerInput(attrs={"class": "form-control"}),
            "medication_time_3": TimePickerInput(attrs={"class": "form-control"}),
            "customer_id": forms.Select(attrs={"class": "form-control"}),
        }

    # First validate if first_name already exists. If so, add name_addon.
    # Second validate if combination of first_name and name_addon exists. If so, get a different name_addon.
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        name_addon = cleaned_data.get("name_addon")
        instance = self.instance

        # Prüfen, ob der first_name bereits existiert
        if Guest.objects.filter(first_name=first_name).exclude(id=instance.id).exists():
            # Wenn kein name_addon eingetragen wurde, einen Fehler auslösen
            if not name_addon:
                self.add_error(
                    "name_addon",
                    "Please provide a name addon as this first name already exists.",
                )
            else:
                # Prüfen, ob die Kombination aus first_name und name_addon existiert
                if (
                    Guest.objects.filter(first_name=first_name, name_addon=name_addon)
                    .exclude(id=instance.id)
                    .exists()
                ):
                    self.add_error(
                        "name_addon",
                        "This combination of first name and name addon already exists. Please choose a different name addon.",
                    )

        return cleaned_data


# Form for checking in guests
class CheckInGuest(forms.ModelForm):
    """_summary_

    Args:
        forms (_type_): _description_
    """

    class Meta:
        model = Presence
        fields = ["guest", "pickup_name"]  # Only the guest field is needed
        labels = {
            "guest": "Guest",
            "pickup_name": "Name of the person picking guest up",
            }
        widgets = {"guest": forms.HiddenInput()}   # Hide the guest field


# Form for checking out guests
class CheckOutGuest(forms.ModelForm):
    """_summary_

    Args:
        forms (_type_): _description_
    """

    class Meta:
        model = Presence
        fields = ["guest"]  # Only the guest field is needed
        labels = {"guest": "Guest"}
        widgets = {"guest": forms.HiddenInput()}  # Hide the guest field
