from tastypie.resources import ModelResource
from analytics.models import Tanker, Driver, Citizen, TrackingData, WaterDispenserData

class DriverResource(ModelResource):
	class Meta:
		queryset = Driver.objects.all()
		resource_name = "driver"

