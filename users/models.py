from django.db import models
from django.db.models import Manager as GeoManager
from django.contrib.gis.db import models
from django.contrib.auth.models import User


class covid_test(models.Model):
    current_status = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.current_status}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    covid = models.ForeignKey(covid_test, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return f'{self.user}'


