from django.db import models
from django.contrib.auth.models import User


STATUS = (
	(0, "Draft"),
	(1, "Publish")
)


class Post(models.Model):
	title = models.CharField(max_length=200, unique=True) # para texto
	slug = models.SlugField(max_length=200, unique=True)
	# Slug is a newspaper term. A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs. 
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
	updated_on = models.DateTimeField(auto_now=True)
	content = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	status = models.IntegerField(choices=STATUS, default=0)

	class Meta:
		# descrescente
		ordering = ['-created_on']
		# abstract = True
		# tabelas abstratas
	
	def __str__(self):
		return self.title
