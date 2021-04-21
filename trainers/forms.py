from django import forms


class TrainerForm(forms.Form):
    description = forms.CharField(max_length=200, required=False, label='Description of what you teach')
    website = forms.URLField(required=False)
    business = forms.CharField(max_length=100, required=False, label='Business Name (Optional)')
    created_on = forms.DateTimeField(widget=forms.HiddenInput())
    last_logged_in = forms.DateTimeField(widget=forms.HiddenInput())

    def save(self):
        new_trainer = Trainer.objects.create(
                description = self.cleaned_data['description'],
                website = self.cleaned_data['website'],
                business = self.cleaned_data['business'],
                created_on = self.cleaned_data['created_on'],
                last_logged_in = self.cleaned_data['last_logged_in'],
        )
        return new_trainer