from django.urls import path

from django.contrib.auth import views as auth_views

from .views import dashboard,register,profile_edit,Profile_view



urlpatterns = [
    path("login/",auth_views.LoginView.as_view(), name="login"),
    path("logout/",auth_views.LogoutView.as_view(), name="logout"),
    path("password_change/",auth_views.PasswordChangeView.as_view(), name = "password_change"),
    path("password_change/done/",auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path("password_reset/",auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/",auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path("password_reset/<uidb64>/<token>/confirm/",auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("password_reset/complete/",auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path("",dashboard, name="dashboard"),
    path("account-register/",register, name="account_register"),
    path("profile_edit/",profile_edit,name="update_profile"),
    path("profile_view/",Profile_view.as_view(),name="profile_view"),


]
