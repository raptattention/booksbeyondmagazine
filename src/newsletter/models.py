from django.db import models

# Create your models here.
class Signup(models.Model):
	email = models.EmailField()
	fullname = models.CharField(max_length=120,blank=False,null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now = False)
	updated = models.DateTimeField(auto_now_add=True, auto_now = False)

	def __unicode__(self):
		return self.email

class Newsletter(models.Model):
	title = models.CharField(max_length=200,blank=True,null=True)
	maintext = models.TextField(blank=True,null=True)
	event1 = models.CharField(max_length=200,blank=True,null=True)
	event1text = models.TextField(blank=True,null=True)
	event2 = models.CharField(max_length=200,blank=True,null=True)
	event2text = models.TextField(blank=True,null=True)
	bookrecommendationtitle = models.CharField(max_length=200,blank=True,null=True)
	bookrecommendationpicture = models.ImageField()
	bookrecommendationdescription = models.TextField(blank=True,null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now = False)
	updated = models.DateTimeField(auto_now_add=True, auto_now = False)

	def __unicode__(self):
		return self.title