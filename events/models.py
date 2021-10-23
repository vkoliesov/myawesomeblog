from django.db import models

class Event(models.Model):
	image = models.ImageField(upload_to='event_images/')
	text = models.CharField(max_length=300)