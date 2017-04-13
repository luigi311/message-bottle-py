from django.shortcuts import render

from django.views.generic import TemplateView, DetailView, ListView, CreateView

from .models import Thread

class HomeView(TemplateView):
    template_name='home.html'

class ThreadCreateView(CreateView):
	model = Thread
	template_name='thread_create.html'
	fields = ['title','message','time_created','time_modified','createdby']
