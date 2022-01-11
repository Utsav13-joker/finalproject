from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Payment(models.Model):
	title = models.CharField(max_length=100)
	amount = models.IntegerField()
	date_of_payment = models.DateTimeField(default=timezone.now)
	customer = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		return self.title