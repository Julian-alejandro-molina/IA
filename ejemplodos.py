import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
df=pd.read_csv('dataset.csv')

x = df['track_name'].tolist()
y = df['valence'].tolist()
n=len(x)
sum_x=sum(x)
sum_Y=sum(y)
productos = [a * b for a, b in zip(x, y)]
x_cuadrado=[ a*a for a,a in zip(x,x)]
df['xi*yi'] = productos
df['x^2'] = x_cuadrado
#df= pd.DataFrame({'X':x, 'Y':y,'xi*yi':productos,'x^2':x_cuadrado})
sumatoria_xiyi=df['xi*yi'].sum()
sumatoria_x2=df['x^2'].sum()

β1 = ((n * sumatoria_xiyi) - (sum_x * sum_Y)) / ((n * sumatoria_x2) - pow(sum_x, 2))
β0 = ((sum_Y*sumatoria_x2)-(sum_x*sumatoria_xiyi))/((n*sumatoria_x2)-pow(sum_x,2))
print("Ecuación de regresión: Y = {:.2f} + {:.2f}X".format(β0, β1))

# Predicción para X = 800
x_pred=800
prediccion = β0 + β1 * x_pred
print("Predicción para X = {}: Y = {:.2f}".format(x_pred,prediccion))


beta1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
beta0 = (sum_y * sum_x2 - sum_x * sum_xy) / (n * sum_x2 - sum_x ** 2)

#  valores predichos
y_pred = beta0 + beta1 * x

#  residuos
residuos = y - y_pred





# Graficar datos y línea de regresión
plt.scatter(x, y, color='blue', label='Datos')
plt.plot(x, [β0 + β1 * xi for xi in x], color='red', label='Línea de regresión')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regresión lineal')
plt.legend()
plt.show()
#print(df,sumatoria_xiyi,sumatoria_x2,β1,β0)

print(df)
print("Sumatoria xi*yi:", sumatoria_xiyi)
print("Sumatoria x^2:", sumatoria_x2)
print("Pendiente (β1):", β1)
print("Intercepto (β0):", β0)

# Graficar el histograma de los residuos
plt.hist(residuos, bins=30, density=True, alpha=0.6, color='g')

# Ajustar y graficar la distribución gaussiana
mu, std = norm.fit(residuos)
xmin, xmax = plt.xlim()
x_gauss = np.linspace(xmin, xmax, 100)
p = norm.pdf(x_gauss, mu, std)
plt.plot(x_gauss, p, 'k', linewidth=2)
title = "Histograma de los residuos\nMedia = {:.2f}, Desviación estándar = {:.2f}".format(mu, std)
plt.title(title)

plt.xlabel('Residuo')
plt.ylabel('Densidad')
plt.show()

# Imprimir la media y la desviación estándar de los residuos
print("Media de los residuos: {:.2f}".format(mu))
print("Desviación estándar de los residuos: {:.2f}".format(std))
