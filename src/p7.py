#! /usr/bin/python
#! encoding: UTF-8
import modulo
t_upla=(10,100,1000,10000,100000,1000000000)
l=[ ]
for e in t_upla:
  x=modulo.aproxpi(e)
  l=l+[x]
  print x
print l

# El número máximo de valores que se pueden introducir en una t_upla son 7.
# Para los elementos mayores a 100000000
#Sí se puede
#Que el archivo con esa extensión puede ser abierto en distintos sistemas operativos.
  