from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views import View
from accounts.forms import RegisterForm, LoginForm
from .models import User
from django.http import Http404
from django.contrib.auth import authenticate, login, logout






class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {'register_form': register_form}
        return render(request, 'accounts/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری است')
            else:
                new_user = User(email=user_email,  is_active=False,
                                username=user_email)
                new_user.set_password(user_password)
                new_user.save()

                return redirect(reverse('login'))

        context = {'register_form': register_form}
        return render(request, 'accounts/register.html', context)


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'accounts/login.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما اکتیو نشده است')
                else:
                    is_password_correct = user.check_password(login_form.cleaned_data.get('password'))
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('home'))
                    else:
                        login_form.add_error('email', 'کاربر یافت نشد')
            else:
                login_form.add_error('email', 'کاربری با مشخصات مورد نظر یافت نشد')

        context = {
            'login_form': login_form
        }
        return render(request, 'accounts/login.html', context)

class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login'))

