from django.db import models

class Driver(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)

class Tanker(models.Model):
	driver = models.ForeignKey(Driver)

class Citizen(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	address = models.TextField()
	latitude = models.FloatField()
	latitude = models.FloatField()

class TrackingData(models.Model):
	tanker = models.ForeignKey(Tanker)
	latitude = models.FloatField()
	longitude = models.FloatField()
	water_level = models.FloatField()
	#speed = models.FloatField()
	time = models.DateTimeField(auto_now_add = True)

class WaterDispenserData(models.Model):
	citizen = models.ForeignKey(Citizen)
	tanker = models.ForeignKey(Tanker)
	time = models.DateTimeField(auto_now_add = True)
	amount = models.FloatField()
	latitude = models.FloatField()
	longitude = models.FloatField()