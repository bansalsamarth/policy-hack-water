import json

from django.shortcuts import render
from django.http import 

from analytics.models import Tanker, Driver, Citizen, TrackingData, WaterDispenserData

def parse_tracking_data(request):
	data = json.load(request.POST['data'])
	track = TrackingData()

	#json = {"id" : 1, "data": ["lat", "long", "water_level", "speed", "time"]}
	tanker_id = data['id']
	track.tanker = Tanker.objects.get(id = int(tanker_id))
	track.latitude = data['data'][0]
	track.longitude = data['data'][1]
	track.water_level = data['data'][2]
	track.speed = data['data'][3]
	track.time = data['data'][4]
	track.save()

	return HttpResponse("Okay", status = 200)

def parse_dispension_data(request):
	data = json.load(request.POST['data'])
	dispension = WaterDispenserData()

	#json = {"id" : 1, "data":["tanker_id", "lat", "long", "amount"]}
	citizen_id = data['citizen_id']
	dispension.citizen = Citizen.objects.get(id = int(citizen_id))

	tanker_id = data['data'][0]
	dispension.tanker = Tanker.objects.get(id = int(tanker_id))

	dispension.latitude = data['data'][1]
	dispension.longitude = data['data'][2]
	amount = data['data'][3]

	return HttpResponse("Okay", status = 200)