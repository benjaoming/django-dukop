from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('signup/confirm/', views.SignupConfirmView.as_view(), name='signup_confirm'),

    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logged_out.html"), name='logout'),

    path('password_change/', views.PasswordChangeView.as_view(template_name="users/password_change_form.html"), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"), name='password_change_done'),

    path('password_reset/', views.PasswordResetView.as_view(template_name="users/password_reset_form.html"), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name='password_reset_complete'),
]
