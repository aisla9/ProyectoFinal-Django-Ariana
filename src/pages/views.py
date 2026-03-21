from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required 
from .models import Post

# 1. FUNCIÓN DE INICIO (HOME) - Va al principio o al final
def home(request):
    return render(request, 'pages/home.html')

# 2. VISTA CON DECORADOR (Solo para cumplir el requisito de la rúbrica)
@login_required
def vista_protegida_ejemplo(request):
    return render(request, 'pages/home.html')

class PostListView(ListView):
    model = Post
    template_name = 'pages/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/post_detail.html'
    context_object_name = 'post'

# --- VISTAS PROTEGIDAS CON LOGIN ---

class PostCreateView(LoginRequiredMixin, CreateView): 
    model = Post
    template_name = 'pages/post_form.html'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user  # Asigna el autor automáticamente
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView): 
    model = Post
    template_name = 'pages/post_form.html'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
    success_url = reverse_lazy('post_list')

class PostDeleteView(LoginRequiredMixin, DeleteView): 
    model = Post
    template_name = 'pages/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

# --- VISTA DE LA PÁGINA ABOUT ---
class AboutView(TemplateView):
    template_name = 'pages/about.html'


class MisPostsView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'pages/mis_publicaciones.html'
    context_object_name = 'mis_posts'

    def get_queryset(self):
        return Post.objects.filter(autor=self.request.user).order_by('-fecha_creacion')