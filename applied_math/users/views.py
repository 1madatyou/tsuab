from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout

from .forms import SignUpForm


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
            print(user_form.errors)
            context.update(
                {'form_errors': user_form.errors}
            )
        
        return self.render_to_response(context)



     
