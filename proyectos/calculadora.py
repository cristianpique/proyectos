#!/usr/bin/python
# -*- encoding: utf-8 -*-

"""Calculadora"""

import os

os.system("clear")
print"\n"

while True:
 print" ========================="
 print"\tCALCULADORA"
 print" ========================="
 print"\ta)Suma"
 print"\tb)Resta"
 print"\tc)Multiplicacio"
 print"\td)Divisio"
 print"\te)Sortir"
 print" ========================="
 print"\n"
 opcio=str(raw_input(" Escull operacio: "))
 print"\n"
 os.system("clear")

 if opcio=="a":
  ns1=int(raw_input(" Introdueix numero 1: "))
  print"\n"
  ns2=int(raw_input(" Introdueix numero 2: "))
  print"\n"
  print"",ns1,"+",ns2,"=",ns1+ns2,
  print"\n"

 if opcio=="b":
  ns1=int(raw_input(" Introdueix numero 1: "))
  print"\n"
  ns2=int(raw_input(" Introdueix numero 2: "))
  print"\n"
  print"",ns1,"-",ns2,"=",ns1-ns2,
  print"\n"

 if opcio=="c":
  ns1=int(raw_input(" Introdueix numero 1: "))
  print"\n"
  ns2=int(raw_input(" Introdueix numero 2: "))
  print"\n"
  print"",ns1,"*",ns2,"=",ns1*ns2,
  print"\n"

 if opcio=="d":
  ns1=int(raw_input(" Introdueix numero 1: "))
  print"\n"
  ns2=int(raw_input(" Introdueix numero 2: "))
  print"\n"
  print"",ns1,"/",ns2,"=",ns1/ns2,
  print"\n"

 if opcio=="e":
  print"\n"
  print" ¡¡¡ Gracies per usar la nostra calculadora. Fins Aviat :) !!!"
  print"\n"
  break
