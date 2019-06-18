from django import forms
from .models import User

class AddUserForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return email
        raise forms.ValidationError('A user with this email already exist')