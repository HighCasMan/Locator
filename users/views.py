from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView, LoginView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from users.forms import UserRegisterForm, UserAuthenticationForm, PasswordReset
from django.views.generic.detail import DetailView
from users.models import Profile
from django.views.generic.edit import CreateView


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


class CreateProfilePageView(CreateView):
    model = Profile

    template_name = 'base/create_profile.html'
    fields = ['profile_pic', 'bio', 'facebook', 'twitter', 'instagram']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('tasks')


class Profile(DetailView):
    model = Profile
    template_name = "account/profile.html"

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(Profile, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context

    def get(self, request):
        context = {
            'form': UserRegisterForm()
        }
        return render(request, self.template_name, context)


class ProfileChange(DetailView):
    pass


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
