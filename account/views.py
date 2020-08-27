from django.contrib import auth
from django.shortcuts import render, redirect

from .forms import RegistrationForm, LoginForm


def login(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = auth.authenticate(request, username=username, password=password)
        if not user:
            return redirect('account/login.html')

        auth.login(request, user)
        return redirect('/')

    return render(request, 'account/login.html', {'form': form})


def register(request):
    form = RegistrationForm(request.POST or None)

    if form.is_valid():
        return redirect('/')

    return render(request, 'account/registration.html', {'form': form})
