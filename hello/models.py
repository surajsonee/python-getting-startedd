from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)
    
class Registration(models.Model):
	title        = models.CharField(max_length=200)
	newstext     = models.CharField(max_length=200)
	newsvideourl = models.CharField(max_length=200)
	#image        = models.FileField(upload_to='static/images')
	fburl        = models.CharField(max_length=200)
	twiterurl    = models.CharField(max_length=200)
	youtubeurl   = models.CharField(max_length=200)

	def __unicode__(self):

	#function returns unicode representaion of a task
		return self.title
