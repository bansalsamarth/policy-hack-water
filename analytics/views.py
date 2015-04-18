import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse

from analytics.models import Tanker, Driver, Citizen, TrackingData, WaterDispenserData

@csrf_exempt
def parse_tracking_data(request):
	data = request.POST
	track = TrackingData()

	#json = {"id" : 1, "data": "lat", "long", "water_level"}
	tanker_id = data['id']
	track.tanker = Tanker.objects.get(id = int(tanker_id))
	a = data['data']
	a = a.split(",")
	track.latitude = a[0]
	track.longitude = a[1]
	track.water_level = a[2]
	track.save()
	a = {"msg" : "Successful"}
	ret = json.dumps(a)
	return HttpResponse(ret, status = 200)

@csrf_exempt
def parse_dispension_data(request):
	data = request.POST
	dispension = WaterDispenserData()

	#json = {"id" : 1, "data":["tanker_id", "lat", "long", "amount"]}
	citizen_id = data['id']
	dispension.citizen = Citizen.objects.get(id = int(citizen_id))

	a = data['data']
	a = a.split(",")

	tanker_id = a[0]
	dispension.tanker = Tanker.objects.get(id = int(tanker_id))

	dispension.latitude = a[1]
	dispension.longitude = a[2]
	dispension.amount = a[3]
	dispension.save()

	return HttpResponse("Okay", status = 200)