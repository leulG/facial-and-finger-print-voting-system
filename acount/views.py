from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserRegistration , UserProfileForm
from .models import Account
from django.contrib.auth import (authenticate ,get_user_model ,login , logout)

# Create your views here.


def registration_view(request):
    if not request.user.is_authenticated:
        title = "Registration"
        form = UserRegistration(request.POST or None)
        profile_form = UserProfileForm(request.POST or None , request.FILES or None )
        if form.is_valid() and profile_form.is_valid():

            user = form.save(commit=False)
            profile = profile_form.save(commit=False)



            password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('username')
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            login(request, user)


            profile.user = request.user
            profile.save()




            return redirect('../')
        context = {
            'title': title,
            'form': form,
            'profile_form' : profile_form,
        }
        return render(request, 'acount/register.html', context)
    return render(request, 'acount/register.html', context={'err': 'Forbidon attempt! sign out first'})