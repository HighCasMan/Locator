from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect
from users.forms import UserRegisterForm, UserAuthenticationForm


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
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class Login(View):
    template_name = 'registration/login.html'

    def get(self, request):
        context = {
            'form': UserAuthenticationForm()
        }
        return render(request, self.template_name, context)


class PasswordReset(View):
    template_name = 'registration/password_reset.html'
