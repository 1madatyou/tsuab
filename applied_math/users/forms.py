from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm


User = get_user_model()

class SignInForm(forms.ModelForm):
    """Форма авторизации"""

    class Meta:
        model = User
        fields = ('email', 'password')


class SignUpForm(forms.ModelForm):
    """Форма регистрации"""
    repeat_password = forms.CharField()

    def clean_repeat_password(self):
        """Проверка на совпадение паролей"""
        cd = self.cleaned_data
        password = cd.get('password')
        repeat_password = cd.get('repeat_password')
        if repeat_password != password:
            print('ПАРОЛИ НЕ СОВПАДАЮТ')
            raise forms.ValidationError('Пароли не совпадают')
        return password

    class Meta:
        model = User
        fields = ('email', 'password', 'name', 'surname', 'patronymic')


class CustomPasswordResetForm(PasswordResetForm):
    """Форма сброса пароля"""
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователя с таким электронным адресом не существует')
        return email
