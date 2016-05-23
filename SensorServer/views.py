from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpRequest
from .models import Walking,MedicationTable
import datetime
from push_notifications.gcm import GCMDevice
from django.db import models

import json
# Create your views here.

def index(request):
    print(datetime.datetime.now())
    return HttpResponse("Test Successful")

def storeWalking(requestObject):
    print(requestObject.body)
    data = json.loads(requestObject.body.decode('utf-8'))
    walking = Walking()
    print("Request \n")
    walking.heart_rate = int(data['HR'])
    walking.time = datetime.datetime.now()
    walking.save()
    print(walking.time)
    return HttpResponse("Posted in Walking table")

def storeMedication(requestObject):
    data = json.loads(requestObject.body.decode('utf-8'))
    medicationTable = MedicationTable()
    walking = Walking()
    walking.time = data['TimeStamp']
    medicationTable.time = walking
    medicationTable.heart_rate = data['HR']
    medicationTable.medication = data['meds']
    medicationTable.save()
    return HttpResponse("Posted at Medication Table")


def storeGCMDevice(requestObject):
    data = json.loads(requestObject.body.decode('utf-8'))
    device = GCMDevice()
    device.device_id = data['device_id']
    device.registration_id = data['registration_id']
    device.name = data['name']
    print("device registered")
    # device.user = data['user'] Join with doctors list if needed later
    return HttpResponse("Device Registered")