from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from accounts.forms import CustomUserCreationForm, CustomAuthenticationForm
from accounts.models import UserProfile


import logging


class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
                user = form.save()
                return redirect('login')
        else:
            logging.warning(form.errors) 
        return render(request, 'register.html', {'form': form})

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'login.html'
    redirect_authenticated_user = True 
    success_url = reverse_lazy('profile')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        profile, _ = UserProfile.objects.get_or_create(user=request.user)
        address = profile  
        return render(request, 'profile.html', {
            'profile': profile,
            'address': address,
        })

    def post(self, request):
        user = request.user
        profile, _ = UserProfile.objects.get_or_create(user=user)

        post_data = request.POST

        if 'first_name' in post_data:
            user.first_name = post_data.get('first_name')
        if 'last_name' in post_data:
            user.last_name = post_data.get('last_name')
        if 'phone' in post_data:
            profile.phone = post_data.get('phone')

        if 'address' in post_data:
            profile.address = post_data.get('address')
        if 'city' in post_data:
            profile.city = post_data.get('city')
        if 'state' in post_data:
            profile.state = post_data.get('state')
        if 'postal_code' in post_data:
            profile.postal_code = post_data.get('postal_code')
        if 'country' in post_data:
            profile.country = post_data.get('country')

        user.save()
        profile.save()

        return redirect('profile')
