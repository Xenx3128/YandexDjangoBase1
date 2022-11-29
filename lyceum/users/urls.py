import django.contrib.auth.views as auth_views
from django.urls import path

from . import views

app_name = 'users'


urlpatterns = [
    path('login/',
         auth_views.LoginView.as_view(
            template_name='users/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(
            template_name='users/logout.html'),
         name='logout'),
    path('password_change/',
         auth_views.PasswordChangeView.as_view(
            template_name='users/password_change.html'),
         name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(
            template_name='users/password_change_done.html'),
         name='password_change_done'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
            template_name='users/password_reset.html'),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
            template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset/confirm/<uidb64>',
         auth_views.PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(
            template_name='users/password_reset_complete.html'),
         name='password_reset_  complete'),
    path('signup/', views.register, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('user_list/', views.user_list, name='user_list'),
    path('user_detail/<int:pk>', views.user_detail, name='user_detail'),
]
