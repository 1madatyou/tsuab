from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import SignIn, SignUp


urlpatterns = [
    path('sign_in', SignIn.as_view(), name='sign_in'),
    path('sign_up', SignUp.as_view(), name='sign_up'),
    
    path('logout/', LogoutView.as_view(next_page='sign_in'), name='logout')
]