import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv('kc_house_data.csv')

# Seleccionar las columnas relevantes
x = df['sqft_living'].values
y = df['price'].values

# Calcular los parámetros de la regresión lineal
n = len(x)
sum_x = sum(x)
sum_y = sum(y)
sum_xy = sum(x * y)
sum_x2 = sum(x ** 2)

beta1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
beta0 = (sum_y * sum_x2 - sum_x * sum_xy) / (n * sum_x2 - sum_x ** 2)

# Imprimir la ecuación de la regresión
print(f"Ecuación de regresión: price = {beta0:.2f} + {beta1:.2f} * sqft_living")

# Predicción para un valor específico de sqft_living
sqft_living_pred = 2000
prediccion = beta0 + beta1 * sqft_living_pred
print(f"Predicción para sqft_living = {sqft_living_pred}: price = {prediccion:.2f}")

# Graficar los datos y la línea de regresión
plt.scatter(x, y, color='blue', label='Datos')
plt.plot(x, beta0 + beta1 * x, color='red', label='Línea de regresión')
plt.xlabel('sqft_living')
plt.ylabel('price')
plt.title('Regresión lineal: Precio vs Tamaño del espacio habitable')
plt.legend()
plt.show()