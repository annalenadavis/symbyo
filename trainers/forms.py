from django import forms
from django.core.exceptions import ValidationError
from .models import User, Trainer, Review

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class TrainerForm(forms.ModelForm):
    # user_id = forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = Trainer
        fields = ('description', 'website', 'business', 'disciplines')
        # hidden field that links trainer with user_id -  grab the current user's id

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('trainer', 'review', 'rating')
