from typing import Any
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

from .forms import SignUpForm, CustomPasswordResetForm


class SignIn(TemplateView):
    """Представление обрабатывающее авторизацию пользователя"""
    template_name = 'users/sign_in.html'

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(
            email=email,
            password=password
        )

        if user:
            login(request, user)
            return redirect('home')
        else:
            context = self.get_context_data()
            context.update(
                {'form_errors': 'Пользователя с такими данными не существует'}
            )
        
        return self.render_to_response(context)


class SignUp(TemplateView):
    """Представление обрабатывающее регистрацию пользователя"""
    template_name = 'users/sign_up.html'

    def post(self, request, *args, **kwargs):
        user_form = SignUpForm(request.POST)
        
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data.get('password'))
            user.save()
            login(request, user)
            return redirect('home')
        else:
            context = self.get_context_data()
            context.update(
                {'form_errors': user_form.errors}
            )
        
        return self.render_to_response(context)
    

class RPD(TemplateView):
    template_name = 'users/reset_password_done.html'


class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/reset_password.html'
    html_email_template_name = 'mail/reset_password_mail.html'
    form_class = CustomPasswordResetForm


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/reset_password_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/reset_password_confirm.html'


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/reset_password_complete.html'



     
