"""
import sys, os

proj_path = "/home/vagrant/webapps/koolproject/"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "koolproject.koolproject.settings")
sys.path.append(proj_path)

os.chdir(proj_path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import obd

from models import OBDdb
"""
import sys, os, django

proj_path = "/home/vagrant/webapps/koolproject"
sys.path.append(proj_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "koolproject.settings")
django.setup()


from readOBD.models import OBDdb

import obd

# connecting ELM
ELMconnection = obd.OBD('/dev/pts/1')

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

    speed = ELMconnection.query(obd.commands.SPEED)
    if not speed.is_null():
        speed = OBDdb.objects.create(speed=speed.value.magnitude)
        speed.save()
        #dataList["SPEED"] = str(speed.value)

    intake_pressure = ELMconnection.query(obd.commands.INTAKE_PRESSURE)
    if not intake_pressure.is_null():
        intake_pressure = OBDdb.objects.create(intake_pressure=intake_pressure.value.magnitude)
        intake_pressure.save()
        #dataList["INTAKE_PRESSURE"] = str(intake_pressure.value)

    intake_temp = ELMconnection.query(obd.commands.INTAKE_TEMP)
    if not intake_temp.is_null():
        intake_temp = OBDdb.objects.create(intake_temp=intake_temp.value.magnitude)
        intake_temp.save()
        #dataList["INTAKE_TEMP"] = str(intake_temp.value)

    rpm = ELMconnection.query(obd.commands.RPM)
    if not rpm.is_null():
        rpm = OBDdb.objects.create(rpm=rpm.value.magnitude)
        rpm.save()
        #dataList["RPM"] = str(rpm.value)

    maf = ELMconnection.query(obd.commands.MAF)
    if not maf.is_null():
        maf = OBDdb.objects.create(maf=maf.value.magnitude)
        maf.save()
        #dataList["MAF"] = str(maf.value)

    coolant_temp = ELMconnection.query(obd.commands.COOLANT_TEMP)
    if not coolant_temp.is_null():
        coolant_temp = OBDdb.objects.create(coolant_temp=coolant_temp.value.magnitude)
        coolant_temp.save()
        #dataList["COOLANT_TEMP"] = str(coolant_temp.value)

    fuel_level = ELMconnection.query(obd.commands.FUEL_LEVEL)
    if not fuel_level.is_null():
        fuel_level = OBDdb.objects.create(fuel_level=coolant_temp.value.magnitude)
        fuel_level.save()
        #dataList["FUEL_LEVEL"] = str(fuel_level.value)

    ambiant_air_temp = ELMconnection.query(obd.commands.AMBIANT_AIR_TEMP)
    if not ambiant_air_temp.is_null():
        ambiant_air_temp = OBDdb.objects.create(ambiant_air_temp=ambiant_air_temp.value.magnitude)
        ambiant_air_temp.save()
        #dataList["AMBIANT_AIR_TEMP"] = str(ambiant_air_temp.value)

    oil_temp = ELMconnection.query(obd.commands.OIL_TEMP)
    if not oil_temp.is_null():
        oil_temp = OBDdb.objects.create(oil_temp=oil_temp.value.magnitude)
        oil_temp.save()
        #dataList["OIL_TEMP"] = str(oil_temp.value)

    control_module_voltage = ELMconnection.query(obd.commands.CONTROL_MODULE_VOLTAGE)
    if not control_module_voltage.is_null():
        control_module_voltage = OBDdb.objects.create(control_module_voltage=control_module_voltage.value.magnitude)
        control_module_voltage.save()
        #dataList["CONTROL_MODULE_VOLTAGE"] = str(control_module_voltage.value)
