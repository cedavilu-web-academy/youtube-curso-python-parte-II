import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos desde Excel - Ruta
datos = pd.read_excel('vendedoras.xlsx')

# Obtener columnas necesarias
nombres = datos['Nombre']
ventas = datos['Ventas']

# Crear el gráfico
# Tipo de gráfico
# plt.bar(nombres,ventas,color='coral')
plt.pie(ventas,labels=nombres, autopct='%1.0f%%',startangle=90)
plt.title('Ventas por persona')
# plt.xlabel('Nombre')
# plt.ylabel('Ventas en $')
plt.tight_layout()

# Mostrar el gráfico
plt.show()
