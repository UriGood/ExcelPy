from xml.etree.ElementInclude import include
from xlrd import open_workbook
from src.conexion_mysql import conexionDb
import pandas as pd 
import os

status = True
excelfiles = []
contenido = os.listdir()
for fichero in contenido:
    if '.xls' in fichero:
        excelfiles.append(fichero)

for file in excelfiles:
    wb = open_workbook(file)
    sheet = wb.sheet_by_index(0)

    for x in range(24):
        serialNumber = sheet.cell_value(49+x, 2)
        meterNo = sheet.cell_value(49+x, 1)
        if(serialNumber != ''):
            panel_number = sheet.cell_value(2, 3)
            job_number = sheet.cell_value(3, 3)
            job_name = sheet.cell_value(4, 3)
            seal = sheet.cell_value(2, 10)
            tipo = sheet.cell_value(27, 1)
            tipo = sheet.cell_value(27, 1)
            modbus_id = sheet.cell_value(32, 2)

            connection = conexionDb()
            # conexion con la base de datos 
            if connection.is_connected():
                status = True
                # info_server = connection.get_server_info()
                # print(info_server)
                cursor = connection.cursor()
                sentencia = "INSERT INTO registros (panel_number,job_number,job_name,seal,type,modbus_id,serial_number,meter_no) VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(
                    panel_number,
                    job_number,
                    job_name,
                    seal,
                    tipo,
                    modbus_id,
                    serialNumber,
                    meterNo
                    )
                cursor.execute(sentencia)
                connection.commit()
        connection.close()
    if(status == True):
        print("registros del documento {0} insertado con exito".format(file))
    else:
        print("error al registrar")   