#from readOBD.models import OBDdb
from django.db import connection

import obd

# connecting ELM
ELMconnection = obd.OBD('/dev/pts/3')

"""
# Check connection status
if connection.status() == OBDStatus.NOT_CONNECTED:
    print("ELM is not connected")

elif connection.status() == OBDStatus.ELM_CONNECTED:
    print("ELM is connected")

elif connection.status() == OBDStatus.CAR_CONNECTED:
    print("Car is connected")
"""
def obddb_custom_sql(dataList):
    sql = """
            INSERT INTO readOBD_obddb (speed,
                                       intake_pressure,
                                       intake_temp,
                                       rpm,
                                       maf,
                                       coolant_temp,
                                       fuel_level,
                                       ambiant_air_temp,
                                       oil_temp,
                                       control_module_voltage)
                                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
          """
    with connection.cursor() as cursor:
        cursor.execute(sql, (dataList[0], dataList[1], dataList[2], dataList[3], dataList[4], dataList[5], dataList[6], dataList[7], dataList[8], dataList[9]))

# Check if a response is empty
while 1:
    dataList = []
    speed = ELMconnection.query(obd.commands.SPEED)
    if not speed.is_null():
        dataList.append(speed.value.magnitude)

    intake_pressure = ELMconnection.query(obd.commands.INTAKE_PRESSURE)
    if not intake_pressure.is_null():
        dataList.append(intake_pressure.value.magnitude)

    intake_temp = ELMconnection.query(obd.commands.INTAKE_TEMP)
    if not intake_temp.is_null():
        dataList.append(intake_temp.value.magnitude)

    rpm = ELMconnection.query(obd.commands.RPM)
    if not rpm.is_null():
        dataList.append(rpm.value.magnitude)

    maf = ELMconnection.query(obd.commands.MAF)
    if not maf.is_null():
        dataList.append(maf.value.magnitude)

    coolant_temp = ELMconnection.query(obd.commands.COOLANT_TEMP)
    if not coolant_temp.is_null():
       dataList.append(coolant_temp.value.magnitude)

    fuel_level = ELMconnection.query(obd.commands.FUEL_LEVEL)
    if not fuel_level.is_null():
       dataList.append(coolant_temp.value.magnitude)

    ambiant_air_temp = ELMconnection.query(obd.commands.AMBIANT_AIR_TEMP)
    if not ambiant_air_temp.is_null():
        dataList.append(ambiant_air_temp.value.magnitude)

    oil_temp = ELMconnection.query(obd.commands.OIL_TEMP)
    if not oil_temp.is_null():
        dataList.append(oil_temp.value.magnitude)

    control_module_voltage = ELMconnection.query(obd.commands.CONTROL_MODULE_VOLTAGE)
    if not control_module_voltage.is_null():
        dataList.append(control_module_voltage.value.magnitude)

    obddb_custom_sql(dataList)
