from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            request.session['username'] = username
            return redirect(reverse('home'))
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})