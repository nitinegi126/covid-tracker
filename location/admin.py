from django.contrib import admin
from location.models import UserLocation, NearByUser
from leaflet.admin import LeafletGeoAdmin


# Register your models here.
class Location_admin(LeafletGeoAdmin):
    list_display = ('user', 'location')


admin.site.register(UserLocation, Location_admin)


class NearUserAdmin(admin.ModelAdmin):
    list_display = ('main', 'close_to')


admin.site.register(NearByUser, NearUserAdmin)
