from django.db import models

# Create your models here.
class Blog(models.Model):
	title=models.CharField(max_length=200)
	content=models.TextField()
	image=models.ImageField(upload_to="B",null=True,blank=True)
	created_date=models.DateTimeField(auto_now_add=True)
	updated_date=models.DateTimeField(auto_now_add=True)
	author=models.CharField(max_length=200,null=True,blank=True)

	def __str__(self):
		return self.title
