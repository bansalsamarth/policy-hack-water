import json

from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
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

from django.utils.dateformat import format

def tanker_data(request, id):
	t = Tanker.objects.get(id = id)
	track = TrackingData.objects.filter(tanker = t)
	ret = {"data" : []}
	for i in track:
		ret['data'].append({
			"latitude" : i.latitude, 
			"longitude": i.longitude,
			"water_level": i.water_level,
			"day" : i.time.day,
			"month":i.time.month,
			"year":i.time.year,
			"hour":i.time.hour,
			"min":i.time.minute,
			"sec":i.time.second,
			})
		
	ret = json.dumps(ret)
	return HttpResponse(ret, content_type = "application/json")

def latest_tanker_data(request):
	t = Tanker.objects.get(id = 1)
	i = TrackingData.objects.filter(tanker = t).order_by('-time')[0]
	ret = {}
	ret['data'] = {
		"latitude" : i.latitude, 
		"longitude": i.longitude,
		"water_level": i.water_level,
		"day" : i.time.day,
		"month":i.time.month,
		"year":i.time.year,
		"hour":i.time.hour,
		"min":i.time.minute,
		"sec":i.time.second,
		}
	ret = json.dumps(ret)
	return HttpResponse(ret, content_type = "application/json")



def main_page(request):
	return render_to_response('index.html', {'active_tab':'live'}, context_instance = RequestContext(request))

def tanker_track(request):
	try:
		id = request.GET['id']
		tanker = Tanker.objects.get(id = id)
	except:
		id = 2
	if int(id) == 1:
		error = False
	else:
		error = True

	return render_to_response('tanker.html', {'active_tab':'tanker', 'error':error}, context_instance = RequestContext(request))

def tanker_delay(request):
	return render_to_response('delay.html', {'active_tab':'delay'}, context_instance = RequestContext(request))

def leakage(request):
	return render_to_response('leakage.html', {'active_tab':'leakage'}, context_instance = RequestContext(request))

def maintainance(request):
	return render_to_response('maintainance.html', {'active_tab':'maintain'}, context_instance = RequestContext(request))
