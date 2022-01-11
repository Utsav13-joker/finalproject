from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm, LoginForm 
from .models import AppUser
# Create your views here.

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			login(request, user)
			messages.success(request, f'Account created for {username}! You are now able to log in')
			return redirect('fyp:fyp-welcome')
		else:
			messages.warning(request, f'Your password does not meet the criteria!')
	form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})

def fyp_login(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, f'You are logged in as { username }')
			return redirect('fyp:fyp-welcome')
		else:
			messages.warning(request, f'The username or password is incorrect')
	else:
		return render(request, 'users/login.html', context={"form": form})

	form = LoginForm()
	return render(request, 'users/login.html', context={"form": form})

def fyp_logout(request):
	logout(request)
	return render(request, 'users/logout.html')
	return redirect('fyp:fyp-logout')
	


def profile(request):
	return render(request, 'users/profile.html')


def add_funds(request):
   
    return render(request, "users/add_funds.html")	