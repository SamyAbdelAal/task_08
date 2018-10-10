from django.db import models

class Restaurant(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	logo= models.ImageField(blank=True, null=True)
	opening_time = models.TimeField()
	closing_time = models.TimeField()
