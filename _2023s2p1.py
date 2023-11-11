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

contenido = [
  {'clave':'%ESTUDIANTE', 'campos':[2,3,1,0,4,5]},
  {'clave':'%SUBTAREAS', 'campos':[10,11,12,13,14]},
  {'clave':'%CONTRATOS', 'campos':[15,16,17,18]},
  {'clave':'%PARAMETROS', 'campos':[19,20,21,22]},
  {'clave':'%HERRAMIENTAS', 'campos':[23,24,25,26,27,28,29]},
  {'clave':'%SINTAXIS', 'campos':[30,31,32,33,34]},
  {'clave':'%RECORRIDOS', 'campos':[35,36,37,38,39,40,41,42]},
  {'clave':'%EJ1', 'campos':[43,44,45,46]},
  {'clave':'%EJ2', 'campos':[47,48,49,50]},
  {'clave':'%EJ3', 'campos':[51,52,53]}
]