from django import forms
from .models import SalesActivity

class SalesActivityForm(forms.ModelForm):
    activity_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    next_follow_up = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = SalesActivity
        fields = ['title', 'operator', 'activity_date', 'description', 'status', 'next_follow_up','sales_representative'
]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['operator'].queryset = self.fields['operator'].queryset.order_by('name')
        self.fields['operator'].label_from_instance = lambda obj: f"{obj.name}"