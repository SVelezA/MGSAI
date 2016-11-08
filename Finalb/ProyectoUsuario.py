#!/usr/bin/python
# -*- coding: latin-1 -*-

import  os
import sys
from Tkinter import *
#import RActProy
#import Form3
#from Form3 import *

master = Tk()
master.geometry("1200x550+0+0")
master.config(bg= "white")
master.title("Aplicativo de Simulacion Costos, Por Santiago Vélez Aristizabal")

guardado = open('pusuario.txt', 'w+')

valor = ""

"///////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#Valor de mi variable según curselection
a1 = "Mantenimiento manual de vias: roceria, limpieza de obras de drenaje, limpieza y reparacion de señales.".split(' ')

a2 = "Mantenimiento mecánico de vias: remocion de derrumbes, perfilado y compactacion de superficie, reconstruccion de cunetas.".split(' ')

a3 = "Mantenimiento rutinario de vias: Incluye las actividades de mantenimiento manual / mecánico, reparacion de baches en afirmado y reparcheos en pavimento".split(' ')

a4 = "Mantenimiento periodico: Incluye las actividades de mantenimiento rutinario; Mantenimiento de obras de drenaje y de paso; Reposicion de pavimento, recuperacion de estructura de pavimento; Recuperacion/reconstruccion de estructura/espesores de afirmado; Construccion de obras de proteccion / muros de contencion; Reconstruccion de obras de drenaje; Recuperacion de señalizacion horizontal y vertical; Mantenimiento de puentes.".split(' ')

a5 = "Rehabilitacion de rasante de vias: Construccion obras de drenaje; Recuperacion/reconstruccion de estructura/espesores de afirmado; Reposicion de pavimento, recuperacion de estructura de pavimento; Construccion obras de estabilizacion de taludes / contencion ".split(' ')

a6 = "Rehabilitacion de puntos criticos viales: Construccion obras de estabilizacion de taludes / contencion; Construccion de calzadas/viaductos otras obras de paso; Construccion obras de estabilizacion de taludes / contencion ".split(' ')

a7 = "Mejoramiento vial: Estabilizacion fisico-quimica de afirmados; Construccion afirmados; Tratamiento superficial doble riego; Pavimentacion pavimento rigido; Pavimentacion pavimento flexible; Rectificacion alineamiento vertical/horizontal; Ampliacion calzada / construccion nuevos carriles; Construccion de obras de drenaje y sub-drenaje (filtros); Reposicion/instalacion señalizacion horizontal; Reposicion/instalacion señalizacion vertical; Reposicion/instalacion iluminacion; Construccion de redes de iluminacion".split(' ')

a8 = "Mantenimiento rutinario de puentes".split(' ')

a9 = "Rehabilitacion estructural de puentes".split(' ')

a10 = "Reposicion de elementos del puente".split(' ')

a11= "Construccion de obras de proteccion de puentes".split(' ')

a12= "Mantenimiento obras de proteccion".split(' ')

a13= "Construccion de puentes".split(' ')

a14= "Pavimentacion de vias urbanas: Construccion de pavimento rigido; Construccion de pavimento flexible; Construccion otros tipo de pavimento; Bacheo; Reparcheos, reconstruccion".split(' ')

a15= "Mantenimiento electromecánico de cables aéreos".split(' ')

a16= "Mantenimiento rutinario y mantenimiento sistemas electromecánicos de túneles".split(' ')

a17= "Construccion de túneles".split(' ')

a18= "Mantenimiento mecánico de vias terciarias".split(' ')

a19= "Construccion de rieles".split(' ')

a20= "Construccion de pavimento placa-huella".split(' ')

a21= "Construccion de obras de iluminacion, obras complementarias".split(' ')

a22= "Construccion de redes de acueducto, alcantarillado".split(' ')

a23= "Construccion de redes de transmision eléctrica".split(' ')

a24= "Mantenimiento de parques municipales / corregimentales".split(' ')

a25= "Reposicion de redes".split(' ')

a26= "Mantenimiento preventivo y correctivo de plazas de mercado y u otras infraestructura municipales.".split(' ')

a27= "Ampliacion de plazas de mercado y u otras infraestructura municipales.".split(' ')

a28= "Estudios y diseños: Estudios y diseños de alternativas técnico-ambientales; Estudios y diseños de pavimento prefactibilidad; Estudios y diseños de pavimento factibilidad; Estudios y diseños de valorizacion prefactibilidad; Estudios y diseños de valorizacion factibilidad; Estudios y diseños puentes; Estudios y diseños de rehabilitacion afirmado; otros estudios".split(' ')

a29= "Construccion de infraestructura de acueducto y alcantarillado: Construccion de todos los elementos que configuran los sistemas de potabilizacion (tanques, desarenadores, floculadores, etc); Construccion de plantas de tratamiento de aguas residuales; Construccion sistemas de bombeo; Construccion de sistemas no convencionales".split(' ')

a30= "Construccion de rellenos sanitarios: Construccion de rellenos sanitarios a cielo abierto; Implementacion planes de abandono; Construccion de plantas de tratamiento de residuos hospitalarios".split(' ')

a31 = "Optimizacion infraestructura de acueducto y alcantarillado: Optimizacion de elementos que configuran los sistemas de potabilizacion (tanques, desarenadores, floculadores, etc); optimizacion de plantas de tratamiento de aguas residuales; Optimizacion de sistemas de bombeo; optimizacion de sistemas no convencionales".split(' ')

a32= "Construccion de vivienda nueva, parques educativos, equipamientos para la prestacion de servicios de salud, culturales/patrimoniales".split(' ')

a33= "Mejoramiento de vivienda".split(' ')

a34= "Reconstruccion (reposicion) / reubicacion de sedes educativas, culturales/patrimoniales".split(' ')

a35= "Mantenimiento preventivo y correctivo de equipamientos educativos, equipamientos para la prestacion de servicios de salud, culturales/patrimoniales".split(' ')

a36= "Ampliacion de equipamientos educativos, equipamientos para la prestacion de servicios de salud, culturales/patrimoniales".split(' ')

a37= "Obras de iluminacion, aire acondicionado, reposicion de redes de servicios domiciliarios".split(' ')

"/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#EVALUAMOS EL VALOR DEL CURSELECT 
tod = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37]

def guardar():
	linea = lista.get(lista.curselection())
	#guardado.seek(0,2)
	g = linea.split()
	x = tod.index(g)
	guardado.write(str(x))
	guardado.close()
	print(x)
	master.destroy()
	import ActividadUsuario


"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#Ciclo que me llena cada linea del listbox con cada linea del Archivo 'text.txt'


def fncLineal():
	archivoLineal.seek(0,0)
	lista.delete(0, END)
	for i in range(25):
		lista.insert(END, archivoLineal.readline())

def fncConcentrado():
	archivoConcentrado.seek(0,0)
	lista.delete(0, END)
	for i in range(25):
		lista.insert(END, archivoConcentrado.readline())



"///////////////////////////////////////////////////////////////////////////////////////////////"

#RADIOBUTTONS

radiobtnlineal = Radiobutton(master, variable = valor, background = "white", text = "Lineal", command = fncLineal, value = 0)
radiobtnlineal.place(x= 50, y = 40)

radiobtncntrado = Radiobutton(master, variable = valor, background = "white", text = "Concentrado", command = fncConcentrado, value = 1)
radiobtncntrado.place(x = 110, y = 40)

"////////////////////////////////////////////////////////////////////////////////////////////////"


txt1 = Label(master, text = 'Por favor, seleccione el tipo de proyecto a desarrollar, luego de la seleccion, haga click en el boton "Seleccionar Actividades"', background = "white")
txt1.place(x = 50, y = 15)

big = Frame(bg = 'Black', height = 372, width = 1120)
big.place(x = 40, y= 70)
lista = Listbox(big, activestyle = 'dotbox', bg = 'white', height = '23', width = 600)
lista.place(x = 0, y = 0)
boton = Button(master, height = 2, width = 20, text = "Seleccionar actividades", command = guardar)
boton.place(x = 840, y = 460)

archivoLineal = open('lineal.txt', 'r')
archivoConcentrado = open('concentrado.txt', 'r')

"////////////////////////////////////////////////////////////////////////////////////////////////////"

for i in range(25):
		lista.insert(END, archivoLineal.readline())
radiobtnlineal.select()

master.mainloop()