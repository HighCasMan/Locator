from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView, LoginView
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect
from django.views.generic import ListView

from users.forms import UserRegisterForm, UserAuthenticationForm, PasswordReset, ProfileForm, CreateLocationsForm
from django.views.generic.base import TemplateView
from users.models import User, Post
from django.views.generic.edit import UpdateView, CreateView


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
    pass


class ProfileView(TemplateView):
    template_name = "account/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['user'] = User.objects.get(id=self.request.user.id)
            return context
        except:
            pass


class ProfileChangeView(UpdateView):
    form_class = ProfileForm
    model = User
    template_name = 'account/profile_change.html'
    success_url = '/users/profile/'

    def get_object(self, queryset=None):
        try:
            obj = User.objects.get(id=self.request.user.id)
            return obj
        except:
            pass


class PasswordResetView(View):
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


class CreateLocationsView(CreateView):
    model = Post
    template_name = "catalog/create_location.html"
    form_class = CreateLocationsForm
    success_url = '/users/profile/'

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.user = User.objects.get(id=self.request.user.id)
        fields.save()
        return super().form_valid(form)


class LocationsView(ListView):
    model = Post
    template_name = "home.html"
