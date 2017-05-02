"""message_bottle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from message_board_app.views import HomeView, ThreadCreateView, UpdateThreadView, ResponseCreateView, ThreadDetailView, ResponseDetailView, UpdateResponseView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^thread/add/$', ThreadCreateView.as_view(), name='thread_add'),
    url(r'^admin/', admin.site.urls),
    url(r'^thread/(?P<pk>\d+)/$', ThreadDetailView.as_view(), name='thread_view'),
    url(r'^response/(?P<pk>\d+)/$', ResponseDetailView.as_view(), name='response_view'),
    url(r'^thread/edit/(?P<pk>\d+)/$', UpdateThreadView.as_view(), name = 'thread_update'),
    url(r'^response/add', ResponseCreateView.as_view(), name='response_add'),
    url(r'^response/edit/(?P<pk>\d+)/$', UpdateResponseView.as_view(), name = 'response_update')
]
