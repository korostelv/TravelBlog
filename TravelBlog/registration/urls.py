
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, profile, edit_profile, delete_profile


app_name = 'registration'

urlpatterns = [


    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('delete_profile/', delete_profile, name='delete_profile')

]

