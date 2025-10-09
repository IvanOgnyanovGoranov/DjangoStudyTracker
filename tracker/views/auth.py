from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View



class LoginView(DjangoLoginView):
    template_name = 'auth/login.html'


class LogoutView(DjangoLogoutView):
    next_page = '/'


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('my_subjects')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})