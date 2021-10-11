from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from djgeojson.views import GeoJSONLayerView
from location.models import UserLocation


urlpatterns = [
    path('', views.home, name="tracker-home"),
    path('signup/', views.signup, name="tracker-signup"),
    path('logout/', views.logout_view, name="tracker-logout"),
    path('login/', auth_views.LoginView.as_view(template_name='users/user_login.html'), name="tracker-login"),
    path('profile/', views.profile, name="tracker-profile"),
    path('check/', views.checkin, name="data-point"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
