from django.forms import ModelForm 
from .models import Patient, Prescription
from django.contrib.auth.models import User
from django import forms

class UserForm(ModelForm):
    class Meta: 
        model = User
        fields = ['first_name', 'last_name', 'email']

class PatientForm(ModelForm):
    class Meta: 
        model = Patient 
        fields = ['birthdate', 'sex', 'doctors']

class PrescriptionForm(ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'
    name = forms.CharField(widget=forms.TextInput
        (attrs={
            "class": "form-control ",
            "id": "prescriptionName",
            "placeholder": "Medication Name"
        }))
    size = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control ",
            "id": "prescriptionStrength",
            "placeholder": "Available Doses"
        }
    ))
    instructions = forms.CharField(widget=forms.Textarea(
        attrs={
            "rows": 3
        }
    ))
    notes = forms.CharField(widget=forms.Textarea(
        attrs={
            "rows": 3
        }
    ))
    notes
    class Meta:
        model = Prescription
        fields = ['name', 'size', 'doctor', 'instructions', 'notes', 'prescribed']

    # def __int__(self, *args, **kwargs):
    #     super().__init__(args, **kwargs)
    #     for field in self.fields:
    #         print(field)
    #         new_data = {
    #             "placeholder": f'Recipe {str(field)}',
    #             "class": "form-control",
                
    #         }

    #         self.fields[str(field)].widget.attrs.update(
    #             new_data
    #         )
    #     self.fields['name'].label = "NAME HERE"
        # self.fields['name'].widget.attrs.update({'class': "form-control-2"})