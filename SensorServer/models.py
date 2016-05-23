from django.db import models
from push_notifications.models import GCMDevice


class Walking(models.Model):
        time = models.DateTimeField('time',primary_key=True)
        heart_rate= models.PositiveSmallIntegerField(name='heart_rate',null=True)

class MedicationTable(models.Model):
        medication = models.TextField(name='medication',primary_key=False,max_length=100,null=True)
        time = models.OneToOneField(Walking, to_field='time')
        heart_rate = models.IntegerField(name='heart_rate',default=-1)
