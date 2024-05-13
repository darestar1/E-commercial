from django import forms
from .models import ReviewRatingg

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRatingg
        fields = ['subject', 'review', 'rating']