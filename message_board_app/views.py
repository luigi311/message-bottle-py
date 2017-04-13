from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView, CreateView ,UpdateView

from .models import Thread

class HomeView(TemplateView):
    template_name='home.html'

class ThreadCreateView(CreateView):
	model = Thread
	template_name='thread_create.html'
	fields = ['title','message','time_created','time_modified','createdby']

class UpdateThreadView(UpdateView):
	model = Thread
	template_name = 'updatethread.html'
	fields = ['title', 'message', 'time_created', 'time_modified', 'createdby']
	
class DetailThreadView(TemplateView):
	model = ThreadView
	template_name='threadview.html'
