#!/usr/bin/python
#!encoding: UTF-8

import sys
import math

PI35DT = 3.1415926535897931159979634685441852

#Utilizacion de una funcion calcular_xi para obtener los xi
def calcular_xi (n, i):
  xi = (i - 1.0/2.0) / n
  return xi
  
#Esta funcion es para calcular los 35 decimales, a su vez llama a la funcion arccot
def decimales_pi(digits):
  unity = 10**(digits + 10)
  decimal_pi = 4 *(8*arccot(5, unity) - arccot(239, unity))
  return (float(decimal_pi // 10**10) / 10 **digits)

def calcular_pi (n):
  #  PI35 = 3.1415926535897931159979634685441852
  sumatorio = 0.0
  ini = 0
  intervalos = 1.0 / float (n)
  for i in range(n):
    x_i = ((i+1) - 1.0/2.0) / n
#   x_i = calcular_xi (n, i+1)
    fx_i = 4.0 /(1.0 + x_i * x_i)
    ini += intervalos
    sumatorio += fx_i
  valor_pi = sumatorio / n
  return (valor_pi)
  
  
#Programa principal
#Ojo, para hacer uso de la funcion sys, debemos incluirla al principio deñ programa

def error (nro_intervalos, nro_test, umbral):
    intervalo = nro_intervalos
    lista = []
    for i in range (nro_test):
      valor = calcular_pi (intervalo)
      intervalo += nro_intervalos
      lista.append (valor)
    pi35 = []
    for i in range (nro_test):
      pi35.append (PI35DT)
    dif35 = []
    for i in range (nro_test):
      dif35.append (abs (pi35[i] - lista[i]))
    correcto = 0
    for i in range (nro_test):
      if (dif35[i] <= umbral):
	correcto = correcto + 1
    porcentaje = 100.0 * (1.0 - (float(correcto) / float (nro_test)))
    return (porcentaje)

if (__name__ == "__main__"):
  argumentos = sys.argv[1:]
  if (len(argumentos) == 3):
    n = int (argumentos[0])
    aproximaciones = int (argumentos[1])
    umbral = float (argumentos[2])
  else:
    print "Introduzca el nº de intervalos(n>0):"
    n = int (raw_input());
    print "Introduce el nº de aproximaciones:"
    aproximaciones = int (raw_input());
    print "Introduce el umbral de error:"
    umbral = float (raw_input ());
  if(n>0):
    porcentaje = error (n, aproximaciones, umbral)
    print"El porcentaje de fallos es del", porcentaje
  else:
    print "El valor de los intervalos debe ser mayor que 0"