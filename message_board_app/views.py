from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView, CreateView ,UpdateView

from .models import Thread, Response, ThreadUser

class HomeView(TemplateView):
    template_name='home.html'

class ThreadCreateView(CreateView): 
	model = Thread
	template_name='thread_create.html'
	fields = ['title','message','createdby']

class UpdateThreadView(UpdateView):
	model = Thread
	template_name = 'updatethread.html'
	fields = ['title','message','createdby']
	
class ThreadDetailView(DetailView):
	model = Thread
	template_name='threadview.html'

class ResponseCreateView(CreateView):
    model = Response
    template_name='respond.html'
    fields = ['title','message','thread','parent_response']

class ResponseDetailView(DetailView):
	model = Response
	template_name='responseview.html'
	
class UpdateResponseView(UpdateView):
	model = Response
	template_name = 'updateresponse.html'
	fields = ['title','message','thread','parent_response']

class UserCreateView(CreateView): 
	model = ThreadUser
	template_name='user_create.html'
	fields = ['thread_user','dob','bio']

class UserUpdateView(UpdateView):
	model = ThreadUser
	template_name = 'user_update.html'
	fields = ['thread_user','dob','bio']
	
class UserDetailView(DetailView):
	model = ThreadUser
	template_name = 'user_view.html'










