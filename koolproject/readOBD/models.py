from django.db import models

class OBDdb(models.Model):
    time = models.DateTimeField(null=True)
    vss = models.FloatField(null=True)
    maf = models.FloatField(null=True)
    rpm = models.FloatField(null=True)
    kpl = models.FloatField(null=True)
    coolant_temp = models.FloatField(null=True)
    oil_temp = models.FloatField(null=True)
    control_module_voltage = models.FloatField(null=True)
    intake_temp = models.FloatField(null=True)
    speed = models.FloatField(null=True)
    intake_pressure = models.FloatField(null=True)

