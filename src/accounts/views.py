from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import PasswordChangeView

from .forms import RegistroForm, UserUpdateForm, PerfilUpdateForm
from .models import Perfil

# 1. Vista de Registro
class SignUpView(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

# 2. Vista de Ver Perfil (Usa Mixin)
class PerfilDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'perfil_user'

    def get_object(self):
        return self.request.user

# 3. Vista de Editar Perfil (Función con decorador de login)
def editar_perfil(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        # Obtenemos o creamos el perfil para evitar errores
        perfil, created = Perfil.objects.get_or_create(user=request.user)
        p_form = PerfilUpdateForm(request.POST, request.FILES, instance=perfil)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        perfil, created = Perfil.objects.get_or_create(user=request.user)
        p_form = PerfilUpdateForm(instance=perfil)

    return render(request, 'accounts/edit_profile.html', {
        'u_form': u_form, 
        'p_form': p_form
    })

# 4. Vista de Cambiar Password
class CambiarPasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('profile')