from django.urls import include ,path
from django.contrib.auth.views import LoginView , LogoutView , logout_then_login

from . import views


app_name = 'Account'

urlpatterns = [
    # ex: /polls/
    path('', views.registration_view, name='register'),
    path('signout/' , LogoutView.as_view() , name = "logout"),
    path('signin/' , LoginView.as_view( template_name='acount/login.html', ) , name = 'Login'),

]