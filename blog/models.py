from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=50)
	date = models.DateTimeField(auto_now_add=True)
	text = models.TextField(max_length=500)
	image=models.ImageField(upload_to='post_images/')