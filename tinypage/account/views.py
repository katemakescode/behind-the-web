from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import LoginForm, RegistrationForm


@login_required(login_url='/account/login')
def profile(request):
    return render(request, 'account/profile.html')


def login(request):
    form = LoginForm(data=request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = auth.authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)

    if request.user.is_authenticated:
        return redirect('account:profile')

    return render(request, 'account/login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return render(request, 'account/logout.html')


def register(request):
    form = RegistrationForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data.get('password'))
        user.save()
        return redirect('/account/login/')

    return render(request, 'account/registration.html', {'form': form})
