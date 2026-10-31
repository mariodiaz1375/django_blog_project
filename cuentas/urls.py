from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from . import views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("registro/", views.registro, name="registro"),
    path("mi_perfil/", views.mi_perfil, name="mi_perfil"),
    path("mi_perfil/editar/", views.editar_perfil, name="editar_perfil"),

    #cambio de contraseña
    path(
        "password/cambiar/", 
        auth_views.PasswordChangeView.as_view(
                template_name="registration/password_change_form.html", 
                success_url=reverse_lazy("password_change_done")
                ), 
        name="password_change"
        ),
    path(
        "password/cambiada/", 
        auth_views.PasswordChangeDoneView.as_view(
                template_name="registration/password_change_done.html"
                ), 
        name="password_change_done"
    ),

    # recuperar contraseña
    path(
        "password/recuperar/",
        auth_views.PasswordResetView.as_view(
            template_name="registration/password_reset_form.html",
            email_template_name="registration/password_reset_email.txt",
            subject_template_name="registration/password_reset_subject.txt",
            success_url=reverse_lazy("password_reset_done")
        ),
        name="password_reset"
    ),
    path(
        "password/recuperar/enviado/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="registration/password_reset_done.html"
        ),
        name="password_reset_done"
    ),
    path(
        "password/recuperar/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="registration/password_reset_confirm.html",
            success_url=reverse_lazy("password_reset_complete")
        ),
        name="password_reset_confirm"
    ),
    path(
        "password/listo/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="registration/password_reset_complete.html"
        ),
        name="password_reset_complete"
    )
]