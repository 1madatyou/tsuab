from django.shortcuts import redirect


def handler404(request, exception):
    """Представление для обработки ошибок 404"""
    return redirect('home')


def home_redirect(request):
    return redirect('home')