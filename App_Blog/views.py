from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from App_Blog.models import Blog, Comment, Likes
from django.urls import reverse, reverse_lazy

# Create your views here.

def blog_list(request):
    return render(request, 'App_Blog/blog_list.html', context={})
