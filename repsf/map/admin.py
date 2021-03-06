from django.contrib import admin
from repsf.map.models import *
from django.http import HttpResponse, HttpResponseForbidden
from actions import export_as_csv_action
from django.contrib import admin
from moderation.admin import ModerationAdmin

class TypeInline(admin.StackedInline):
    model = Type

class LocationAdmin(ModerationAdmin):
	list_display = ['name', 'address','get_types_for_admin','fix_address']
	actions = [export_as_csv_action("CSV Export", fields=['name','address','get_types_for_admin','fix_address'])]
	inlines = [TypeInline,]

admin.site.register(Location, LocationAdmin)

class TypeAdmin(admin.ModelAdmin):
	list_display = ['name', 'label']

admin.site.register(Type, TypeAdmin)