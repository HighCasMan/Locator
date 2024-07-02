from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView, LoginView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect
from users.forms import UserRegisterForm, UserAuthenticationForm, PasswordReset


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserRegisterForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('/')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class Login(LoginView):
    template_name = 'registration/login.html'
    form_class = UserAuthenticationForm


class Logout(LogoutView):
    template_name = "registration/logout.html"


class Profile(View):
    template_name = "registration/profile.html"


class PasswordReset(View):
    email_template_name = "registration/password_reset_email.html"
    form_class = PasswordReset
    success_url = "password_reset_done"
    template_name = "registration/password_reset_form.html"


INTERNAL_RESET_SESSION_TOKEN = "_password_reset_token"


class PasswordResetDone(View):
    template_name = "registration/password_reset_done.html"
    title = "Password reset sent"


class PasswordChange(View):
    template_name = 'registration/password_change.html'


class PasswordChangeDone(View):
    template_name = 'registration/password_change_Done.html'
