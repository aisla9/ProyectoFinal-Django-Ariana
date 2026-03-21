from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUpView, PerfilDetailView, editar_perfil, CambiarPasswordView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='post_list'), name='logout'),
    path('registro/', SignUpView.as_view(), name='signup'),
    path('perfil/', PerfilDetailView.as_view(), name='profile'),
    path('perfil/editar/', editar_perfil, name='profile_edit'),
    path('perfil/password/', CambiarPasswordView.as_view(), name='change_password'),
]