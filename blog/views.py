from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post
from django.urls import reverse_lazy

class BlogListView(ListView):
    template_name = 'home.html'
    model = Post

class BlogDetailView(DetailView):
    template_name = 'post_details.html'
    model = Post

class BlogCreateView(CreateView):
    template_name = 'post_create.html'
    model = Post
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    template_name = 'post_update.html'
    model = Post
    fields = ['title', 'author', 'body']

class BlogDeleteView(DeleteView):
    template_name = 'post_delete.html'
    model = Post
    fields = ['title', 'author', 'body']
    success_url = reverse_lazy('home')
