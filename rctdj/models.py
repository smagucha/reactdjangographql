from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=50)

	def __str__(self):
		return '{} {}'.format(self.name,self.description)


class Buses(models.Model):
	name = models.CharField(max_length=50)
	seat = models.PositiveIntegerField()

	class Meta:
		verbose_name_plural = "Buses"

	def __str__(self):
		return "{}".format(self.name)


class Routes(models.Model):
	name = models.CharField(max_length=50)
	From = models.CharField(max_length=50)
	To =models.CharField(max_length=50, blank=True, null=True)

	class Meta:
		verbose_name_plural = "Routes"

	def __str__(self):
		return "{}".format(self.name)


class Customer(models.Model):
	firstname = models.CharField(max_length=50)
	lastname=models.CharField(max_length=50)
	IDNumber =models.CharField(max_length=50)
	phone = models.CharField(max_length=50)
	email = models.EmailField(blank=True, null=True)
	cus = models.ForeignKey(User, on_delete=models.CASCADE)


class Ticket(models.Model):
	firstname = models.CharField(max_length=50)
	lastname=models.CharField(max_length=50)
	IDNumber =models.CharField(max_length=50)
	phone = models.CharField(max_length=50)
	seat =  models.CharField(max_length=50)
	routes =  models.ForeignKey(Routes, on_delete=models.CASCADE)
	cus = models.ForeignKey(User, on_delete=models.CASCADE)

# class Paymentmethod(models.Model):
# 	pass






