from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=350)
    category = models.CharField(max_length=255, default='')
    sub_heading = models.CharField(max_length=500, blank=True)
    content_1 = models.CharField(max_length=9999, blank=True)
    content_2 = models.CharField(max_length=9999, blank=True)
    content_3 = models.CharField(max_length=9999, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Category(models.Model):
	name = models.CharField(max_length=255, default='')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'categories'
    

