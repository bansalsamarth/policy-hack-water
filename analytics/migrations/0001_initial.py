# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Driver'
        db.create_table(u'analytics_driver', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'analytics', ['Driver'])

        # Adding model 'Tanker'
        db.create_table(u'analytics_tanker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('driver', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analytics.Driver'])),
        ))
        db.send_create_signal(u'analytics', ['Tanker'])

        # Adding model 'Citizen'
        db.create_table(u'analytics_citizen', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'analytics', ['Citizen'])

        # Adding model 'TrackingData'
        db.create_table(u'analytics_trackingdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tanker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analytics.Tanker'])),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('water_level', self.gf('django.db.models.fields.FloatField')()),
            ('speed', self.gf('django.db.models.fields.FloatField')()),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'analytics', ['TrackingData'])

        # Adding model 'WaterDispenserData'
        db.create_table(u'analytics_waterdispenserdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('citizen', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analytics.Citizen'])),
            ('tanker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analytics.Tanker'])),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('amount', self.gf('django.db.models.fields.FloatField')()),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'analytics', ['WaterDispenserData'])


    def backwards(self, orm):
        # Deleting model 'Driver'
        db.delete_table(u'analytics_driver')

        # Deleting model 'Tanker'
        db.delete_table(u'analytics_tanker')

        # Deleting model 'Citizen'
        db.delete_table(u'analytics_citizen')

        # Deleting model 'TrackingData'
        db.delete_table(u'analytics_trackingdata')

        # Deleting model 'WaterDispenserData'
        db.delete_table(u'analytics_waterdispenserdata')


    models = {
        u'analytics.citizen': {
            'Meta': {'object_name': 'Citizen'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'latitude': ('django.db.models.fields.FloatField', [], {})
        },
        u'analytics.driver': {
            'Meta': {'object_name': 'Driver'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'analytics.tanker': {
            'Meta': {'object_name': 'Tanker'},
            'driver': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analytics.Driver']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'analytics.trackingdata': {
            'Meta': {'object_name': 'TrackingData'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'speed': ('django.db.models.fields.FloatField', [], {}),
            'tanker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analytics.Tanker']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'water_level': ('django.db.models.fields.FloatField', [], {})
        },
        u'analytics.waterdispenserdata': {
            'Meta': {'object_name': 'WaterDispenserData'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'citizen': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analytics.Citizen']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'tanker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analytics.Tanker']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['analytics']