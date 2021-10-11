from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
from django.contrib.auth.models import User


# Create your models here.
class UserLocation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.PointField(srid=4326)
    ip_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    objects = GeoManager()

    def __unicode__(self):
        return self.user


class NearByUser(models.Model):
    main = models.ForeignKey(User, on_delete=models.CASCADE)
    close_to = models.CharField(max_length=255)
    time = models.TimeField()

