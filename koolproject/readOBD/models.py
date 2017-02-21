import sys
try:
    from django.db import models
except Exception:
    print("There was an error loading django modules. Do you have djanog installed?")
    sys.exit()

class OBDdb(models.Model):
    local_time = models.DateTimeField(auto_now_add=True, null=True)
    #car_time = models.DateTimeField()
    #vss = models.FloatField(null=True)
    maf = models.FloatField(null=True)
    rpm = models.FloatField(null=True)
    #kpl = models.FloatField(null=True)
    coolant_temp = models.FloatField(null=True)
    oil_temp = models.FloatField(null=True)
    control_module_voltage = models.FloatField(null=True)
    intake_temp = models.FloatField(null=True)
    speed = models.FloatField(null=True)
    intake_pressure = models.FloatField(null=True)
    fuel_level = models.FloatField(null=True)
    ambiant_air_temp = models.FloatField(null=True)

