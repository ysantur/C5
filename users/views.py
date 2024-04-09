# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_view(request):
    logout(request)
    return redirect('home')

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UserUpdateView(generic.UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('home')
    template_name = 'registration/update.html'

    # This keeps users from accessing the profile of other users.
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return CustomUser.objects.all()
        else:
            return CustomUser.objects.filter(id=user.id)

class UserPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('home')
    template_name = 'registration/change_password.html'

class UserPasswordResetView(PasswordResetView):
    success_url = reverse_lazy('login')
    template_name = 'registration/reset_password.html'
