import random

from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView

from users.forms import UserRegisterForm, UserForm
from users.models import User
from users.services import send_verify_email


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):

    def get_success_url(self):
        return reverse_lazy("well:home")


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    # def form_valid(self, form):
    #     new_user = form.save(commit=False)
    #     new_user.verification_token = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    #     new_user.save()
    #     send_verify_email(self.request, new_user.verification_token, new_user.email)
    #     return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm
    template_name = 'users/user_form.html'

    def get_object(self, queryset=None):
        return self.request.user


class UserListView(ListView):
    model = User
