# -*- coding: utf-8 -*-

anio = '2023'
semestre = '2do'
evaluacion = 'Primer recuperatorio'

contenido = [
  {'clave':'%ESTUDIANTE', 'campos':[2,3,1,0,4,5,9,10]},
  {'clave':'%SUBTAREAS', 'campos':[26,27,28,29,30,32]},
  {'clave':'%CONTRATOS', 'campos':[40,41,42,43,46]},
  {'clave':'%PARAMETROS', 'campos':[33,34,35,36,39]},
  {'clave':'%HERRAMIENTAS', 'campos':[19,20,21,22,23,25]},
  {'clave':'%ESTILO', 'campos':[54,55,56,57,60]},
  {'clave':'%RECORRIDOS', 'campos':[47,48,49,50,53]},
  {'clave':'%EJ1', 'campos':[11,12]},
  {'clave':'%EJ2', 'campos':[14,15]},
  {'clave':'%EJ3', 'campos':[17]}
]

rubrica = '''
Universidad Nacional de Quilmes - Introducción a la Programación - ''' + evaluacion + ' - ' + semestre + ' Semestre de ' + anio + '''

\\

\estudiante%ESTUDIANTE

\\begin{minipage}{0.5\\textwidth}

\ejercicio{1}%EJ1

\ejercicioTres%EJ3

\contratos%CONTRATOS

\\recorridos%RECORRIDOS

\estilo%ESTILO

\end{minipage} \\begin{minipage}{0.52\\textwidth}

\ejercicio{2}%EJ2

\subtareas%SUBTAREAS

\parametros%PARAMETROS

\herramientas%HERRAMIENTAS

\end{minipage}

\\newpage
'''