from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Main thread class 
class Thread(models.Model):
  title = models.CharField(max_length=255) # Title of the thread
  message = models.TextField() # Thread message, large text should use TextField instead of CharField
  time_created = models.DateTimeField(auto_now=False,auto_now_add=True) # Timestamp of when the thread was first created 
  time_modified = models.DateTimeField(auto_now=True,auto_now_add=False) # Timestamp for when the thread was last modified

  def __str__(self):
    return self.title

# Response class that corresponds to a main thread
class Response(models.Model):
  title = models.CharField(max_length=255) # Title of the response
  message = models.TextField() # Response message
  time_created = models.DateTimeField(auto_now=False,auto_now_add=True) # Timestamp of when a response was first created
  time_modified = models.DateTimeField(auto_now=True,auto_now_add=False) # Timestamp of when a response was last modified

  def __str__(self):
    return self.title

# User class that will contain all the users
class User(models.Model):
  username = models.CharField(max_length=255) # Internet alias of the user
  first_name = models.CharField(max_length=255) # First name of the user
  last_name = models.CharField(max_length=255) # Last name of the user
  dob = models.DateField(auto_now=False,auto_now_add=False) # Date of Birth for the user
  creation = models.DateTimeField(auto_now=False,auto_now_add=True) # When the user was first created
  bio = models.TextField() # Bio about the user to allow them to share information about themselfs to others.

  def __str__(self):
    return self.username

# Class that will link the User class to the Thread class in order to show the creator
class ThreadCreation(models.Model):
  thread = models.ForeignKey(Thread) # Points to the Thread class 
  creator = models.ForeignKey(Response) # Points to the Response class

  def __str__(self):
    return self.thread

# Class that will link the User class to the Response class in order to show the creator and link to the Thread class to show the corresponding thread
class ResponseCreation(models.Model):
  thread = models.ForeignKey(Thread) # Points to the Thread class 
  response = models.ForeignKey(Response) # Points to the Response class 
  creator = models.ForeignKey(User) # Points to the User class 

  def __str__(self):
    return self.response
