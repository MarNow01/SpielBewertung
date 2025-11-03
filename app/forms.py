from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'content']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'content': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'rating': 'Ocena (1–10)',
            'content': 'Treść recenzji',
        }
