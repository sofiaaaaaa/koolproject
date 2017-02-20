import obd
#import json
#from django.db import models

from readOBD.models import OBDdb
#import requests

#from obd import OBDStatus

# connecting ELM
connection = obd.OBD('/dev/pts/1')

"""
# Check connection status
if connection.status() == OBDStatus.NOT_CONNECTED:
    print("ELM is not connected")

elif connection.status() == OBDStatus.ELM_CONNECTED:
    print("ELM is connected")

elif connection.status() == OBDStatus.CAR_CONNECTED:
    print("Car is connected")
"""

# Check if a response is empty
while 1:
    #dataList = {}

    speed = connection.query(obd.commands.SPEED)
    if not speed.is_null():
        speed = OBDdb.objects.create(speed=speed.value.magnitude)
        speed.save()
        #dataList["SPEED"] = str(speed.value)

    intake_pressure = connection.query(obd.commands.INTAKE_PRESSURE)
    if not intake_pressure.is_null():
        intake_pressure = OBDdb.objects.create(intake_pressure=intake_pressure.value.magnitude)
        intake_pressure.save()
        #dataList["INTAKE_PRESSURE"] = str(intake_pressure.value)

    intake_temp = connection.query(obd.commands.INTAKE_TEMP)
    if not intake_temp.is_null():
        intake_temp = OBDdb.objects.create(intake_temp=intake_temp.value.magnitude)
        intake_temp.save()
        #dataList["INTAKE_TEMP"] = str(intake_temp.value)

    rpm = connection.query(obd.commands.RPM)
    if not rpm.is_null():
        rpm = OBDdb.objects.create(rpm=rpm.value.magnitude)
        rpm.save()
        #dataList["RPM"] = str(rpm.value)

    maf = connection.query(obd.commands.MAF)
    if not maf.is_null():
        maf = OBDdb.objects.create(maf=maf.value.magnitude)
        maf.save()
        #dataList["MAF"] = str(maf.value)

    coolant_temp = connection.query(obd.commands.COOLANT_TEMP)
    if not coolant_temp.is_null():
        coolant_temp = OBDdb.objects.create(coolant_temp=coolant_temp.value.magnitude)
        coolant_temp.save()
        #dataList["COOLANT_TEMP"] = str(coolant_temp.value)

    fuel_level = connection.query(obd.commands.FUEL_LEVEL)
    if not fuel_level.is_null():
        fuel_level = OBDdb.objects.create(fuel_level=coolant_temp.value.magnitude)
        fuel_level.save()
        #dataList["FUEL_LEVEL"] = str(fuel_level.value)

    ambiant_air_temp = connection.query(obd.commands.AMBIANT_AIR_TEMP)
    if not ambiant_air_temp.is_null():
        ambiant_air_temp = OBDdb.objects.create(ambiant_air_temp=ambiant_air_temp.value.magnitude)
        ambiant_air_temp.save()
        #dataList["AMBIANT_AIR_TEMP"] = str(ambiant_air_temp.value)

    oil_temp = connection.query(obd.commands.OIL_TEMP)
    if not oil_temp.is_null():
        oil_temp = OBDdb.objects.create(oil_temp=oil_temp.value.magnitude)
        oil_temp.save()
        #dataList["OIL_TEMP"] = str(oil_temp.value)

    control_module_voltage = connection.query(obd.commands.CONTROL_MODULE_VOLTAGE)
    if not control_module_voltage.is_null():
        control_module_voltage = OBDdb.objects.create(control_module_voltage=control_module_voltage.value.magnitude)
        control_module_voltage.save()
        #dataList["CONTROL_MODULE_VOLTAGE"] = str(control_module_voltage.value)
