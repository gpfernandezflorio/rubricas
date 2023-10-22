rubrica = '''
\estudiante%ESTUDIANTE

\\begin{minipage}{0.5\\textwidth}

\subtareas%SUBTAREAS

\contratos%CONTRATOS

\parametros%PARAMETROS

\herramientas%HERRAMIENTAS

\end{minipage} \\begin{minipage}{0.6\\textwidth}

\sintaxis%SINTAXIS

\\recorridos%RECORRIDOS

\ejercicio{1}%EJ1

\ejercicio{2}%EJ2

\ejercicioTres%EJ3

\end{minipage}

\\newpage
'''

import csv
csvreader = csv.reader(open('data.csv'))

salida = ''

for row in csvreader:
  while len(row) < 54:
    row.append('')
  salida += rubrica.replace(
    '%ESTUDIANTE', '{' + row[2] + ', ' + row[3] + '}{' + row[1] + '}{' + row[0] + '}{' + row[4] + '}{' + row[5] + '}'
  ).replace(
    '%SUBTAREAS', '{' + row[10] + '}{' + row[11] + '}{' + row[12] + '}{' + row[13] + '}{' + row[14] + '}'
  ).replace(
    '%CONTRATOS', '{' + row[15] + '}{' + row[16] + '}{' + row[17] + '}{' + row[18] + '}'
  ).replace(
    '%PARAMETROS', '{' + row[19] + '}{' + row[20] + '}{' + row[21] + '}{' + row[22] + '}'
  ).replace(
    '%HERRAMIENTAS', '{' + row[23] + '}{' + row[24] + '}{' + row[25] + '}{' + row[26] + '}{' + row[27] + '}{' + row[28] + '}{' + row[29] + '}'
  ).replace(
    '%SINTAXIS', '{' + row[30] + '}{' + row[31] + '}{' + row[32] + '}{' + row[33] + '}{' + row[34] + '}'
  ).replace(
    '%RECORRIDOS', '{' + row[35] + '}{' + row[36] + '}{' + row[37] + '}{' + row[38] + '}{' + row[39] + '}{' + row[40] + '}{' + row[41] + '}{' + row[42] + '}'
  ).replace(
    '%EJ1', '{' + row[43] + '}{' + row[44] + '}{' + row[45] + '}{' + row[46] + '}'
  ).replace(
    '%EJ2', '{' + row[47] + '}{' + row[48] + '}{' + row[49] + '}{' + row[50] + '}'
  ).replace(
    '%EJ3', '{' + row[51] + '}{' + row[52] + '}{' + row[53] + '}'
  )

f = open('rubricas.tex', 'w')
f.write(salida)
f.close()