from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Mensaje

# Vista para ver los mensajes recibidos
class InboxView(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = 'messenger/inbox.html'
    context_object_name = 'mensajes'

    def get_queryset(self):
        # Solo muestra los mensajes donde el usuario actual es el receptor
        return Mensaje.objects.filter(receptor=self.request.user).order_by('-fecha')

# Vista para enviar un mensaje
class SendMessageView(LoginRequiredMixin, CreateView):
    model = Mensaje
    fields = ['receptor', 'contenido']
    template_name = 'messenger/send_message.html'
    success_url = reverse_lazy('inbox')

    def form_valid(self, form):
        # Asignamos automáticamente al usuario logueado como el emisor
        form.instance.emisor = self.request.user
        return super().form_valid(form)
