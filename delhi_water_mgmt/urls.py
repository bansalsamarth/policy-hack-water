from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api

from analytics.api import DriverResource, TankerResource, CitizenResource, DispensingDataResource, TrackingResource
from analytics.views import parse_tracking_data, parse_dispension_data

v1_api = Api(api_name = 'v1')
v1_api.register(DriverResource())
v1_api.register(TrackingResource())
v1_api.register(TankerResource())
v1_api.register((CitizenResource()))
v1_api.register((DispensingDataResource()))


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^dispense/', parse_dispension_data),
    url(r'^track/', parse_tracking_data)
)