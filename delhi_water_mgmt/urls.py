from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api

from analytics.api import DriverResource, TankerResource, CitizenResource, DispensingDataResource, TrackingResource
from analytics.views import latest_tanker_data, tanker_data, parse_tracking_data, parse_dispension_data, main_page, tanker_track, tanker_delay, leakage, maintainance

v1_api = Api(api_name = 'v1')
v1_api.register(DriverResource())
v1_api.register(TrackingResource())
v1_api.register(TankerResource())
v1_api.register((CitizenResource()))
v1_api.register((DispensingDataResource()))


urlpatterns = patterns('',

	url(r'^$', main_page),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^dispense/', parse_dispension_data),
    url(r'^track/', parse_tracking_data),
    url(r'^tanker/', tanker_track),
    url(r'^delay/', tanker_delay),
    url(r'^maintain/', maintainance),
    url(r'^leakage/', leakage),
    url(r'^api/v1/tanker_data/(?P<id>\d+)', tanker_data),
    url(r'^latest_tanker_data', latest_tanker_data),
)