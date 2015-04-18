from tastypie.resources import ModelResource
from tastypie import fields

from analytics.models import Tanker, Driver, Citizen, TrackingData, WaterDispenserData

class DriverResource(ModelResource):
	class Meta:
		queryset = Driver.objects.all()
		resource_name = "driver"

class TankerResource(ModelResource):
	class Meta:
		queryset = Tanker.objects.all()
		resource_name = "tanker"

class CitizenResource(ModelResource):
	class Meta:
		queryset = Citizen.objects.all()
		resource_name = "citizen"

class DispensingDataResource(ModelResource):
	citizen = fields.ForeignKey(CitizenResource, 'citizen')
	tanker = fields.ForeignKey(TankerResource, 'tanker')
	class Meta:
		queryset = WaterDispenserData.objects.all()
		resource_name = "dispenser"

class TrackingResource(ModelResource):
	tanker = fields.ForeignKey(TankerResource, 'tanker')
	class Meta:
		queryset = TrackingData.objects.all()
		resource_name = "track"