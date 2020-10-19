from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from ask.models import Profile,Question,Poll,Answer,Comment


class RegistrationForm(UserCreationForm):
    title = forms.CharField(
        max_length = 300,
        label = "Title",
        widget = forms.TextInput(attrs = {'class' : 'input-field','placeholder': 'Title'}))
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class' : 'input-field','placeholder': 'Password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class' : 'input-field','placeholder': 'Confirm Password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    
    class Meta:
        model = User
        fields = ['username','first_name','password1','password2','title']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-field','placeholder': 'Email'}),
            'first_name' : forms.TextInput(attrs = {'class' : 'input-field','placeholder': 'Full Name'}),
        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        print(self.cleaned_data['username'])
        print(self.cleaned_data['first_name'])
        print(self.cleaned_data['password1'])
        print(self.cleaned_data['title'])
        user_profile = Profile(user=user,title=self.cleaned_data['title'])
        if commit:
            user.save()
            user_profile.save()
        return user, user_profile