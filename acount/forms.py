from django import forms
from .models import Account

from django.contrib.auth import (authenticate ,get_user_model ,login , logout)

user = get_user_model()
class UserRegistration(forms.ModelForm):
    email = forms.EmailField(label='email adress')
    email2 = forms.EmailField(label='confirm email adress')
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = user
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'email2',
            'password',

        ]
    '''
      def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')

        if commit:
            user.save()
        return user
    '''


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            "profile_pic",
            "adress",
        ]