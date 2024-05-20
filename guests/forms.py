from django import forms
from .models import Guest


class AddGuest(forms.ModelForm):
    class Meta:
        model = Guest
        fields = (
            'first_name',
            'last_name',
            'name_addon',
            'gender',
            'image',
            'date_of_birth',
            'information',
            'food',
            'food_time_1',
            'food_time_2',
            'food_time_3',
            'medication',
            'medication_time_1',
            'medication_time_2',
            'medication_time_3',
            'customer_id'
            )
        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'name_addon': 'Name addon',
            'gender': 'Gender',
            'image': 'Image',
            'date_of_birth' : 'Date of Birth',
            'information': 'Information',
            'food': 'Food',
            'food_time_1': 'Food time 1',
            'food_time_2': 'Food time 2',
            'food_time_3': 'Food time 3',
            'medication': 'Medication',
            'medication_time_1': 'Medication time 1',
            'medication_time_2': 'Medication time 2',
            'medication_time_3': 'Medication time 3',
            'customer_id': '',
        }
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'name_addon': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'date_of_birth' : forms.DateInput(attrs={'class': 'form-control'}),
            'information': forms.Textarea(attrs={'class': 'form-control'}),
#            'food': forms.SelectMultiple(attrs={'class': 'form-control'}),
#            'food_time_1': forms.TimeField(attrs={'class': 'form-control'}),
#            'food_time_2': forms.TimeField(attrs={'class': 'form-control'}),
#            'food_time_3': forms.TimeField(attrs={'class': 'form-control'}),
#            'medication': forms.SelectMultiple(attrs={'class': 'form-control'}),
#            'medication_time_1': forms.TimeField(attrs={'class': 'form-control'}),
#            'medication_time_2': forms.TimeField(attrs={'class': 'form-control'}),
#            'medication_time_3': forms.TimeField(attrs={'class': 'form-control'}),
            'customer_id': forms.Select(attrs={'class': 'form-control'}),
        }
        
        
        
