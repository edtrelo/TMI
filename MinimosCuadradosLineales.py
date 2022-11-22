import numpy as np

def ajustarRecta(xdata, ydata):
  """Ajusta una recta al conjunto de datos (x_i, y_i)."""
  # obtenemos el tamaño del conjunto
  n = len(xdata)
  m = len(ydata)
  # verificamos que las variables dependientes tengan el mismo tamaño que las variables independientes.
  if n != m:
    raise ValueError("Las dimensiones de los arreglos no coinciden.")
  # transformamos los arreglos a unos de numpy.
  x_n = np.array(xdata)
  y_n = np.array(xdata)
  # obtenemos las sumas
  Sum_x = sum(x_n)
  Sum_y = sum(y_n)
  Sum_xx = sum(x_n**2)
  Sum_xy = sum(x_n*y_n)
  # obtenemos los parámetros
  a = (n*Sum_xy-Sum_x*Sum_y)/(n*Sum_xx-Sum_x**2)
  b = (Sum_xx*Sum_y-Sum_xy*Sum_x)/(n*Sum_xx-Sum_x**2)
  # listo!
  return a, b
