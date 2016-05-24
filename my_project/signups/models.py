from __future__ import unicode_literals

from django.db import models
from django.utils import  timezone
from django.utils.encoding import smart_unicode
# Create your models here.

class SignUp(models.Model):
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField()
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    updated_time = models.DateField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.email)

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
                default=timezone.now)
    published_date = models.DateTimeField(
                blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title