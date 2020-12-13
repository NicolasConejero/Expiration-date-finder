from tkinter import *
import datetime
import os
import sys

root = Tk()
root.title("Fecha Factoring")
root.geometry("1200x1200")

texto_0 = Label(root, text = "Control de Gestión OTZI SPA\n\n")
texto_0.grid(row = 0, column = 0)

texto_inicial = str(datetime.date.today())

texto_00 = Label(root, text = (texto_inicial + "\n\n"))
texto_00.grid(row = 0, column = 2)

texto_1 = Label(root, text = "\n\nEn este programa se podrá calcular la fecha de vencimiento a solicitar a los factoring. Tenemos cuatro opciones.")
texto_1.grid(row = 0, column = 1)





dia_de_hoy = datetime.date.today()


#------------------------- 15 DIAS ---------------------------------------------
#15 DIAS


texto_15_dias = Label(root, text = "\n\n(1). Fecha de vencimiento en 15 dias")
texto_15_dias.grid(row = 1, column = 1)

tmedelta_15 = datetime.timedelta(days=15)
fecha_en_15_dias = (dia_de_hoy + tmedelta_15)
fecha_en_15_ISO = fecha_en_15_dias.isoweekday()

tmedelta_caso_lunes_15 = datetime.timedelta(days=4)
fecha_si_cae_lunes_15 = (fecha_en_15_dias + tmedelta_caso_lunes_15)

tmedelta_caso_martes_15 = datetime.timedelta(days=3)
fecha_si_cae_martes_15 = (fecha_en_15_dias + tmedelta_caso_martes_15)

tmedelta_caso_miercoles_15 = datetime.timedelta(days=2)
fecha_si_cae_miercoles_15 = (fecha_en_15_dias + tmedelta_caso_miercoles_15)

tmedelta_caso_jueves_15 = datetime.timedelta(days=1)
fecha_si_cae_jueves_15 = (fecha_en_15_dias + tmedelta_caso_jueves_15)

tmedelta_caso_sabado_15 = datetime.timedelta(days=6)
fecha_si_cae_sabado_15 = (fecha_en_15_dias + tmedelta_caso_sabado_15)

tmedelta_caso_domingo_15 = datetime.timedelta(days=5)
fecha_si_cae_domingo_15 = (fecha_en_15_dias + tmedelta_caso_domingo_15)

if fecha_en_15_ISO == 1 :
    texto_dia_semana_15 = "Lunes"
if fecha_en_15_ISO == 2 :
    texto_dia_semana_15 = "Martes"
if fecha_en_15_ISO == 3 :
    texto_dia_semana_15 = "Miercoles"
if fecha_en_15_ISO == 4 :
    texto_dia_semana_15 = "Jueves"
if fecha_en_15_ISO == 5 :
    texto_dia_semana_15 = "Viernes"
if fecha_en_15_ISO == 6 :
    texto_dia_semana_15 = "Sabado"
if fecha_en_15_ISO == 7 :
    texto_dia_semana_15 = "Domingo"

if fecha_en_15_ISO == 1:
    texto_final_15 = ("\nEl viernes mas cercano seria el: " + str(fecha_si_cae_lunes_15))

if fecha_en_15_ISO == 2:
    texto_final_15 = ("\nEl viernes mas cercano seria el: " + str(fecha_si_cae_martes_15))

if fecha_en_15_ISO == 3:
    texto_final_15 = ("\nEl viernes mas cercano seria el: " + str(fecha_si_cae_miercoles_15))

if fecha_en_15_ISO == 4:
    texto_final_15 = ("\nEl viernes mas cercano seria el: " + str(fecha_si_cae_jueves_15))

if fecha_en_15_ISO == 6:
    texto_final_15 = ("\nEl viernes mas cercano seria el: " + str(fecha_si_cae_sabado_15))

if fecha_en_15_ISO == 5:
    texto_final_15 = ("\nEl viernes mas cercano seria el: " + str(fecha_si_cae_domingo_15))


def funcion_boton_15():
    calculo_fecha_15_dias = Label(root, text = str("Fecha en 15 dias [AAAA/MM/DD]: " + str(fecha_en_15_dias)))
    calculo_fecha_15_dias.grid(row = 3, column = 1)
    calculo_fecha_15_dias_dia_de_semana = Label(root, text=str("Dia de la semana en que cae: " + str(texto_dia_semana_15) + str("\n\n " + texto_final_15)))
    calculo_fecha_15_dias_dia_de_semana.grid(row = 4, column = 1)

button = Button(root, text = "Calculo fecha de vencimiento en 15 dias", fg = "red" , command = funcion_boton_15)
button.grid(row = 2, column = 1)

#------------------------- 30 DIAS ---------------------------------------------

#30 DIAS

texto_30_dias = Label(root, text = "\n\n(1). Fecha de vencimiento en 30 dias")
texto_30_dias.grid(row = 5, column = 1)

tmedelta_30 = datetime.timedelta(days=30)
fecha_en_30_dias = (dia_de_hoy + tmedelta_30)
fecha_en_30_ISO = fecha_en_30_dias.isoweekday()

tmedelta_caso_lunes_30 = datetime.timedelta(days=4)
fecha_si_cae_lunes_30= (fecha_en_30_dias + tmedelta_caso_lunes_30)

tmedelta_caso_martes_30 = datetime.timedelta(days=3)
fecha_si_cae_martes_30 = (fecha_en_30_dias + tmedelta_caso_martes_30)

tmedelta_caso_miercoles_30 = datetime.timedelta(days=2)
fecha_si_cae_miercoles_30 = (fecha_en_30_dias + tmedelta_caso_miercoles_30)

tmedelta_caso_jueves_30 = datetime.timedelta(days=1)
fecha_si_cae_jueves_30 = (fecha_en_30_dias + tmedelta_caso_jueves_30)

tmedelta_caso_sabado_30 = datetime.timedelta(days=6)
fecha_si_cae_sabado_30 = (fecha_en_30_dias + tmedelta_caso_sabado_30)

tmedelta_caso_domingo_30 = datetime.timedelta(days=5)
fecha_si_cae_domingo_30 = (fecha_en_30_dias + tmedelta_caso_domingo_30)

if fecha_en_30_ISO == 1 :
    texto_dia_semana_30 = "Lunes"
if fecha_en_30_ISO == 2 :
    texto_dia_semana_30 = "Martes"
if fecha_en_30_ISO == 3 :
    texto_dia_semana_30 = "Miercoles"
if fecha_en_30_ISO == 4 :
    texto_dia_semana_30 = "Jueves"
if fecha_en_30_ISO == 5 :
    texto_dia_semana_30 = "Viernes"
if fecha_en_30_ISO == 6 :
    texto_dia_semana_30 = "Sabado"
if fecha_en_30_ISO == 7 :
    texto_dia_semana_30 = "Domingo"

if fecha_en_30_ISO == 1:
    texto_final_30 = ("\nEl viernes mas cercano seria el: " + str(fecha_si_cae_lunes_30))

if fecha_en_30_ISO == 2:
    texto_final_30 = ("\nEl viernes mas cercano seria el: " + str(fecha_si_cae_martes_30))

if fecha_en_30_ISO == 3:
    texto_final_30 = ("\nEl viernes mas cercano seria el: " + str(fecha_si_cae_miercoles_30))

if fecha_en_30_ISO == 4:
    texto_final_30 = ("\nEl viernes mas cercano seria el: " + str(fecha_si_cae_jueves_30))

if fecha_en_30_ISO == 6:
    texto_final_30 = ("\nEl viernes mas cercano seria el: " + str(fecha_si_cae_sabado_30))

if fecha_en_30_ISO == 5:
    texto_final_30 = ("\nEl viernes mas cercano seria el: " + str(fecha_si_cae_domingo_30))


def funcion_boton_30():
    calculo_fecha_30_dias = Label(root, text = str("Fecha en 30 dias [AAAA/MM/DD]: " + str(fecha_en_30_dias)))
    calculo_fecha_30_dias.grid(row = 7, column = 1)
    calculo_fecha_30_dias_dia_de_semana = Label(root, text=str("Dia de la semana en que cae: " + str(texto_dia_semana_30) + str("\n\n " + texto_final_30)))
    calculo_fecha_30_dias_dia_de_semana.grid(row = 8, column = 1)

button = Button(root, text = "Calculo fecha de vencimiento en 30 dias", fg = "red" , command = funcion_boton_30)
button.grid(row = 6, column = 1)

#------------------------- 60 DIAS ---------------------------------------------

#60 DIAS

texto_60_dias = Label(root, text = "\n\n(1). Fecha de vencimiento en 60 dias")
texto_60_dias.grid(row = 9, column = 1)

tmedelta_60 = datetime.timedelta(days=60)
fecha_en_60_dias = (dia_de_hoy + tmedelta_60)
fecha_en_60_ISO = fecha_en_60_dias.isoweekday()

tmedelta_caso_lunes_60 = datetime.timedelta(days=4)
fecha_si_cae_lunes_60= (fecha_en_60_dias + tmedelta_caso_lunes_60)

tmedelta_caso_martes_60 = datetime.timedelta(days=3)
fecha_si_cae_martes_60 = (fecha_en_60_dias + tmedelta_caso_martes_60)

tmedelta_caso_miercoles_60 = datetime.timedelta(days=2)
fecha_si_cae_miercoles_60 = (fecha_en_60_dias + tmedelta_caso_miercoles_60)

tmedelta_caso_jueves_60 = datetime.timedelta(days=1)
fecha_si_cae_jueves_60 = (fecha_en_60_dias + tmedelta_caso_jueves_60)

tmedelta_caso_sabado_60 = datetime.timedelta(days=6)
fecha_si_cae_sabado_60 = (fecha_en_60_dias + tmedelta_caso_sabado_60)

tmedelta_caso_domingo_60 = datetime.timedelta(days=5)
fecha_si_cae_domingo_60 = (fecha_en_60_dias + tmedelta_caso_domingo_60)

if fecha_en_60_ISO == 1 :
    texto_dia_semana_60 = "Lunes"
if fecha_en_60_ISO == 2 :
    texto_dia_semana_60 = "Martes"
if fecha_en_60_ISO == 3 :
    texto_dia_semana_60 = "Miercoles"
if fecha_en_60_ISO == 4 :
    texto_dia_semana_60 = "Jueves"
if fecha_en_60_ISO == 5 :
    texto_dia_semana_60 = "Viernes"
if fecha_en_60_ISO == 6 :
    texto_dia_semana_60 = "Sabado"
if fecha_en_60_ISO == 7 :
    texto_dia_semana_60 = "Domingo"

if fecha_en_60_ISO == 1:
    texto_final_60 = ("\nEl viernes mas cercano seria el: " + str(fecha_si_cae_lunes_60))

if fecha_en_60_ISO == 2:
    texto_final_60 = ("\nEl viernes mas cercano seria el: " + str(fecha_si_cae_martes_60))

if fecha_en_60_ISO == 3:
    texto_final_60 = ("\nEl viernes mas cercano seria el: " + str(fecha_si_cae_miercoles_60))

if fecha_en_60_ISO == 4:
    texto_final_60 = ("\nEl viernes mas cercano seria el: " + str(fecha_si_cae_jueves_60))

if fecha_en_60_ISO == 6:
    texto_final_60 = ("\nEl viernes mas cercano seria el: " + str(fecha_si_cae_sabado_60))

if fecha_en_60_ISO == 5:
    texto_final_60 = ("\nEl viernes mas cercano seria el: " + str(fecha_si_cae_domingo_60))


def funcion_boton_60():
    calculo_fecha_60_dias = Label(root, text = str("Fecha en 60 dias [AAAA/MM/DD]: " + str(fecha_en_60_dias)))
    calculo_fecha_60_dias.grid(row = 11, column = 1)
    calculo_fecha_60_dias_dia_de_semana = Label(root, text=str("Dia de la semana en que cae: " + str(texto_dia_semana_60) + str("\n\n " + texto_final_60)))
    calculo_fecha_60_dias_dia_de_semana.grid(row = 12, column = 1)

button = Button(root, text = "Calculo fecha de vencimiento en 60 dias", fg = "red" , command = funcion_boton_60)
button.grid(row = 10, column = 1)

#------------------------- 90 DIAS ---------------------------------------------

#90 DIAS

texto_90_dias = Label(root, text = "\n\n(1). Fecha de vencimiento en 90 dias")
texto_90_dias.grid(row = 14, column = 1)

tmedelta_90 = datetime.timedelta(days=90)
fecha_en_90_dias = (dia_de_hoy + tmedelta_90)
fecha_en_90_ISO = fecha_en_90_dias.isoweekday()

tmedelta_caso_lunes_90 = datetime.timedelta(days=4)
fecha_si_cae_lunes_90= (fecha_en_90_dias + tmedelta_caso_lunes_90)

tmedelta_caso_martes_90 = datetime.timedelta(days=3)
fecha_si_cae_martes_90 = (fecha_en_90_dias + tmedelta_caso_martes_90)

tmedelta_caso_miercoles_90 = datetime.timedelta(days=2)
fecha_si_cae_miercoles_90 = (fecha_en_90_dias + tmedelta_caso_miercoles_90)

tmedelta_caso_jueves_90 = datetime.timedelta(days=1)
fecha_si_cae_jueves_90 = (fecha_en_90_dias + tmedelta_caso_jueves_90)

tmedelta_caso_sabado_90 = datetime.timedelta(days=6)
fecha_si_cae_sabado_90 = (fecha_en_90_dias + tmedelta_caso_sabado_90)

tmedelta_caso_domingo_90 = datetime.timedelta(days=5)
fecha_si_cae_domingo_90 = (fecha_en_90_dias + tmedelta_caso_domingo_90)

if fecha_en_90_ISO == 1 :
    texto_dia_semana_90 = "Lunes"
if fecha_en_90_ISO == 2 :
    texto_dia_semana_90 = "Martes"
if fecha_en_90_ISO == 3 :
    texto_dia_semana_90 = "Miercoles"
if fecha_en_90_ISO == 4 :
    texto_dia_semana_90 = "Jueves"
if fecha_en_90_ISO == 5 :
    texto_dia_semana_90 = "Viernes"
if fecha_en_90_ISO == 6 :
    texto_dia_semana_90 = "Sabado"
if fecha_en_90_ISO == 7 :
    texto_dia_semana_90 = "Domingo"

if fecha_en_90_ISO == 1:
    texto_final_90 = ("\nEl viernes mas cercano seria el: " + str(fecha_si_cae_lunes_90))

if fecha_en_90_ISO == 2:
    texto_final_90 = ("\nEl viernes mas cercano seria el: " + str(fecha_si_cae_martes_90))

if fecha_en_90_ISO == 3:
    texto_final_90 = ("\nEl viernes mas cercano seria el: " + str(fecha_si_cae_miercoles_90))

if fecha_en_90_ISO == 4:
    texto_final_90 = ("\nEl viernes mas cercano seria el: " + str(fecha_si_cae_jueves_90))

if fecha_en_90_ISO == 6:
    texto_final_90 = ("\nEl viernes mas cercano seria el: " + str(fecha_si_cae_sabado_90))

if fecha_en_90_ISO == 5:
    texto_final_90 = ("\nEl viernes mas cercano seria el: " + str(fecha_si_cae_domingo_90))


def funcion_boton_90():
    calculo_fecha_90_dias = Label(root, text = str("Fecha en 90 dias [AAAA/MM/DD]: " + str(fecha_en_90_dias)))
    calculo_fecha_90_dias.grid(row = 16, column = 1)
    calculo_fecha_90_dias_dia_de_semana = Label(root, text=str("Dia de la semana en que cae: " + str(texto_dia_semana_90) + str("\n\n " + texto_final_90)))
    calculo_fecha_90_dias_dia_de_semana.grid(row = 17, column = 1)

button = Button(root, text = "Calculo fecha de vencimiento en 90 dias", fg = "red" , command = funcion_boton_90)
button.grid(row = 15, column = 1)


mainloop()