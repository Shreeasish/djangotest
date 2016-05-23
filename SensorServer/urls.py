from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'post-walking-medication/', csrf_exempt(views.storeMedication)),
    url(r'post-walking/', csrf_exempt(views.storeWalking)),
    url(r'register-device-android/',csrf_exempt(views.storeGCMDevice)),
]