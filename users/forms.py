from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.utils.translation import gettext_lazy as _

from users.models import Post

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
        model = get_user_model()
        fields = ["username", "email", "password1", "password2"]


class UserAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label=_("Email"),
                                max_length=254,
                                widget=forms.EmailInput(attrs={"class": "input-wrapper",
                                                               "placeholder": "enter email"}))

    password = forms.CharField(widget=forms.TextInput(attrs={"class": "input-wrapper",
                                                             "type": "text",
                                                             "placeholder": "enter password"}))

    class Meta(AuthenticationForm):
        model = get_user_model()
        fields = ['email', 'password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email', 'username', 'bio',
            'profile_pic', 'facebook',
            'twitter', 'instagram'
        ]


class PasswordReset(AuthenticationForm):
    pass


class CreateLocationsForm(forms.ModelForm):
    description = forms.CharField(label=_("Description"), max_length=254, )
    photo = forms.FileField

    class Meta:
        model = Post
        fields = ['description', 'photo']
