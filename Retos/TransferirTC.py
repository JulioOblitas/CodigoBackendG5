# -*- coding: utf-8 -*-
from os import getcwd
import xlrd
import pyodbc
from datetime import datetime




opcion = input('SEGURO DE PROCESAR TIPO DE CAMBIO S/N: ')
if (opcion == "S"):

    data = xlrd.open_workbook("D:\\JOCODIGOBACKENDG5\\TC.xlsx")
    sheettc = data.sheet_by_index(0)
    sheetempresas = data.sheet_by_index(1)

    empresas = 1
    for empresas  in range(sheetempresas.nrows):
        ruta =  sheetempresas.cell_value(empresas,0)

        # Nombre del controlador.
        DRIVER_NAME = "Microsoft Access Driver (*.mdb, *.accdb)"
        DB_PATH = ruta

        conn = pyodbc.connect("Driver={%s};DBQ=%s;" % (DRIVER_NAME, DB_PATH))

        # Crear cursor para ejecutar consultas.

        cursor = conn.cursor()
        for i in range(sheettc.nrows):
            
            if  (i >0 ):
                estado = sheettc.cell_value(i,3)
                if (estado == "P"):
                    fecha = sheettc.cell_value(i,0)
                    tccompra = sheettc.cell_value(i,1)
                    tcventa = sheettc.cell_value(i,2)
            
            
                    # Agregar algunos datos.
                    # Ejecutar la consulta.
                    cursor.execute(u"INSERT INTO MDH_TC  ( fecha, tc, tv "
                u") VALUES (?, ?, ? )",fecha,  tccompra,tcventa,)
                    # Guardar los cambios.
                    cursor.commit()
            
        cursor.close()
        conn.close()

print("Proceso Terminado para ", (empresas + 1)  , "empresas")
#Ejecutar  un consulta
#q = cursor.execute("SELECT * FROM empleados")
#rows = q.fetchall()

    








    


