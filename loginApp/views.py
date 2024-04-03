from django.contrib.auth.decorators import login_required
from loginApp.forms import UserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from loginApp.models import UserProfile


# Create your views here.

def sign_up_view(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            password = form.cleaned_data.get('password1')
            user_profile = UserProfile.objects.create(user=user, name=username, email=email, phone=phone,
                                                      password=password)
            user_profile.save()
            return redirect('movieRatingApp:home')
    return render(request, 'loginApp/sign_up.html', context={'form': form})


def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('movieRatingApp:home')

    return render(request, 'loginApp/login.html', context={'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('movieRatingApp:index')
