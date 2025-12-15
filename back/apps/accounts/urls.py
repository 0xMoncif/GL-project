from django.urls import path
from .views import RegisterView,LoginView,UserView
urlpatterns = [
    path('users/',UserView.as_view(), name='get_users'),
    path('register/',RegisterView.as_view(), name='register'),
    path('login/',LoginView.as_view() , name='login')
]