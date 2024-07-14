from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView, LoginView
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from users.forms import UserRegisterForm, UserAuthenticationForm, PasswordReset, ProfileForm
from django.views.generic.detail import DetailView
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
    template_name = "registration/logout.html"


class ProfileView(DetailView):
    model = User
    template_name = "account/profile.html"
    context_object_name = "profile"


class ProfileChangeView(UpdateView):
    form_class = ProfileForm
    model = User
    template_name = 'account/profile_change.html'

    def get_success_url(self, **kwargs):
        return reverse("profile", kwargs={'pk': self.object.pk})


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
    fields = '__all__'

# class LocationsView(ListView):
#     model = Post
#     template_name = "catalog/start_page.html"
#
    # def get(self, request):
    #     context = {"111"}
    #     return render(request, self.template_name, context)
