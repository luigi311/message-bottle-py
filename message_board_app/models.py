from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse


# Main thread class 
class Thread(models.Model):
    title = models.CharField(max_length=255) # Title of the thread
    message = models.TextField() # Thread message, large text should use TextField instead of CharField
    time_created = models.DateTimeField(auto_now=False,auto_now_add=True) # Timestamp of when the thread was first created 
    time_modified = models.DateTimeField(auto_now=True,auto_now_add=False) # Timestamp for when the thread was last modified
    createdby = models.ForeignKey(User)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('thread_view', kwargs={'pk': self.pk})


# Response class that corresponds to a main thread
class Response(models.Model):
    title = models.CharField(max_length=255) 
    message = models.TextField()
    time_created = models.DateTimeField(auto_now=False,auto_now_add=True) 
    time_modified = models.DateTimeField(auto_now=True,auto_now_add=False)
    createdby = models.ForeignKey(User, related_name="user_responses")
    thread = models.ForeignKey(Thread)
    parent_response = models.ForeignKey('Response', blank=True, null=True, default=None, related_name='responses')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('response_view', kwargs={'pk':self.pk})

# User class that extends auth.models.User 
class ThreadUser(models.Model):
    thread_user = models.OneToOneField(User)
    dob = models.DateField(auto_now=False,auto_now_add=False) # Date of Birth for the user
    bio = models.TextField() # Bio about the user to allow them to share information about themselfs to others.

    def __str__(self):
        return self.thread_user.user.username
    def get_absolute_url(self):
        return reverse('user_view', kwargs={'pk':self.pk})




