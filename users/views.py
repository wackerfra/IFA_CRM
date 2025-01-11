from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm


# def register_user(request):
#     """
#     Register a new user.
#     """
#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Log in the user after signing up
#             return redirect('report_list')
#     else:
#         form = CustomUserCreationForm()
#
#     return render(request, 'users/register.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the custom user
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')  # Redirect to login page
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})


class CustomLoginView(LoginView):
    """
    Custom login view.
    """
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('report_list')



@login_required
def logout_user(request):
    """
    Log out the current user.
    """
    logout(request)
    return redirect('login')
