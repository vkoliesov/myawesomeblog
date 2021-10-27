from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=50)
	date = models.DateTimeField(auto_now_add=True)
	text = models.TextField()
	image=models.ImageField(upload_to='post_images/')


	def __str__(self):
		return self.title


	def get_summary(self):
		return self.text[:100]