from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    check_in = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    check_out = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    option_until = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    confirmed_at = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Booking
        fields = ['operator', 'hotel','double_rooms', 'single_rooms',  'segment',
                   'check_in', 'check_out', 'number_of_guests', 'total_price', 'option_until',
                  'confirmed_at', 'cancelation_terms', 'payment_terms','sales_representative'
]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['operator'].queryset = self.fields['operator'].queryset.order_by('name')
        self.fields['operator'].label_from_instance = lambda obj: f"{obj.name}"