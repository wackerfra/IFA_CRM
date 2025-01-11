from django import forms
from .models import Operator

class OperatorForm(forms.ModelForm):
    class Meta:
        model = Operator
        fields = [
            'name', 'contact_person', 'phone', 'email',
            'street', 'house_no', 'zip', 'city', 'country', 'special_conditions'
        ]
