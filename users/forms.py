from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserRegisterForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={"class": "input-wrapper",
                                                             "type": "text",
                                                             "placeholder": "enter username"}))

    email = forms.EmailField(label=_("Email"),
                             max_length=254,
                             widget=forms.EmailInput(attrs={"class": "input-wrapper",
                                                            "placeholder": "enter email"}))

    password1 = forms.CharField(widget=forms.TextInput(attrs={"class": "input-wrapper",
                                                              "type": "text",
                                                              "placeholder": "enter password"}))

    password2 = forms.CharField(widget=forms.TextInput(attrs={"class": "input-wrapper",
                                                              "type": "text",
                                                              "placeholder": "enter password again"}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserAuthenticationForm(AuthenticationForm):

    email = forms.EmailField(label=_("Email"),
                             max_length=254,
                             widget=forms.EmailInput(attrs={"class": "input-wrapper",
                                                            "placeholder": "enter email"}))

    password = forms.CharField(widget=forms.TextInput(attrs={"class": "input-wrapper",
                                                             "type": "text",
                                                             "placeholder": "enter password"}))

    class Meta(AuthenticationForm):
        model = User
        fields = ['email', 'password']
