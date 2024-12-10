from django import forms
from.models import Property


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'title', 'description', 'price', 'status',
            'bedrooms', 'bathrooms', 'square_feet', 'location'
        ]


