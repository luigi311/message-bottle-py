from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView, CreateView ,UpdateView

from .models import Thread, Response

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
	
class ThreadDetailView(DetailView):
	model = Thread
	template_name='threadview.html'

class ResponseCreateView(CreateView):
    model = Response
    template_name='respond.html'
    fields = ['title','message','thread','parent_response']

class UpdateResponseView(UpdateView):
	model = Response
	template_name = 'updateresponse.html'
	fields = ['title','message','thread','parent_response']

