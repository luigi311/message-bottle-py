from django.shortcuts import render

from django.views.generic import TemplateView, DetailView, ListView, UpdateView



from .models import Thread

class HomeView(TemplateView):
    template_name='home.html'







class UpdateThreadView(UpdateView):
	model = Thread
	template_name = 'updatethread.html'
	fields = ['title', 'message', 'time_created', 'time_modified', 'createdby']