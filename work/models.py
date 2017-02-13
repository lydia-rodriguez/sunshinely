from django.db import models
from django.utils import timezone

class Site(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	description = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	
	def __str__(self):
		return self.title
		
class Contact(models.Model):
	first_name = models.CharField(max_length=80)
	last_name = models.CharField(max_length=120)
	email = models.EmailField(max_length=254)
	subject = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	sent_date = models.DateTimeField(blank=True, null=True)
	
	def send(self):
		self.sent_date = timezone.now()
		self.save()
	
	def __str__(self):
		return self.subject