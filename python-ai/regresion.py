from sklearn.linear_model import LinearRegression

import numpy as np

# Datos de entrada (x) y salida (y)
x = np.array([[1],[2],[3],[4]])
y = np.array([2,4,6,8])

# Crear un modelo
modelo = LinearRegression()

# Entrenar el modelo
modelo.fit(x,y)

# Hacer una predicción
print('Predicción para x = 5', modelo.predict([[5]]))

# Fijese como el modelo logra descubrir la formula
print('Descubrio la formula: (coef_):' , modelo.coef_)