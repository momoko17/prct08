#!/usr/bin/python
#!encoding: UTF-8
import sys
import modulo

argumentos = sys.argv[1:]
if (len(argumentos) == 8):
  n = int (argumentos[0])
  aproximaciones = int (argumentos[1])
  umbral = []
  for i in range (2,7):
    umbral.append(float (argumentos[i]))
  nombre_fichero = argumentos[7]
else:
  print "Introduzca el nº de intervalos(n>0):"
  n = int (raw_input());
  print "Introduce el nº de aproximaciones:"
  aproximaciones = int (raw_input());
  print "Introduce 5 umbrales de error:"
  umbral = []
  for i in range (5):
    print "Introduce el umbral", i,":"
    umbral.append(float (raw_input()));
  print "Introduce el nombre del fichero para almacenar los resultados:"
  nombre_fichero = raw_input ();
if(n>0):
#Una forma de averiguar si un fichero existe o no puede ser esta:
#debemos incluir el paquete os.path
#if os.path.isfile(nombre_fichero):
#	fichero = open (nombre_fichero,"a")
#else:
#	fichero = open (nombre_fichero, "w")
#Otra forma puede ser mediante excepciones, como vemos a continuacion:
  try:
    fichero = open (nombre_fichero, "a")
  except:
    fichero = open (nombre_fichero, "w")
  fichero.write ("Nº de intervalos: %d\n" % (aproximaciones))
  for i in range (5):
    porcentaje = modulo.error (n, aproximaciones,umbral[i])
    fichero.write ("%2.2f%% de fallos para el umbral %2.5f\n" % (porcentaje, umbral[i]))
  fichero.close()
else:
  print "El valor de los intervalos debe ser mayor que 0"