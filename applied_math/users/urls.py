from django.urls import path
from django.contrib.auth.views import (
    LogoutView, 
)

from .views import (
    SignIn, 
    SignUp, 
    RPD, 
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView,
)


urlpatterns = [
    path('sign_in', SignIn.as_view(), name='sign_in'),
    path('sign_up', SignUp.as_view(), name='sign_up'),
    path('rpd', RPD.as_view()),
    
    path('logout/', LogoutView.as_view(next_page='sign_in'), name='logout'),

    path('reset_password', CustomPasswordResetView.as_view(), name='reset_password'),
    path('password_reset/done', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/"', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),      
    path('password_reset/complete"', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),        
]

# reset_password - введите адрес почты
# reset_password_done - письмо отправлено
# reset_password_confirm - введите новый пароль
# reset_password_complete - пароль изменен
