# from _2023s2p1 import *
from _2023s2r1 import *

import csv
csvreader = csv.reader(open('data.csv'))

salida = ''

import functools 
m = 1 + max(functools.reduce(lambda rec, x : rec + x['campos'], contenido, []))

def args(r, campos):
  return ''.join(map(lambda x : '{' + r[x] + '}', campos))

def fila(r):
  return lambda rec, x : rec.replace(x['clave'], args(r, x['campos']))

def pagina(r):
  return functools.reduce(fila(r), contenido, rubrica)

for row in csvreader:
  while len(row) < m:
    row.append('')
  salida += pagina(row)

f = open('rubricas.tex', 'w')
f.write(salida.replace('%', '\%'))
f.close()