import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x = [5000, 5570, 4350, 7900, 6800, 5400, 6900, 3900, 4200, 5780]
y = [160000, 189380, 139200, 260700, 217600, 183600, 234600, 136500, 138600, 202300]
n=10
sum_x=sum(x)
sum_Y=sum(y)
productos = [a * b for a, b in zip(x, y)]
x_cuadrado=[ a*a for a,a in zip(x,x)]
df= pd.DataFrame({'X':x, 'Y':y,'xi*yi':productos,'x^2':x_cuadrado})
sumatoria_xiyi=df['xi*yi'].sum()
sumatoria_x2=df['x^2'].sum()

β1 = ((n * sumatoria_xiyi) - (sum_x * sum_Y)) / ((n * sumatoria_x2) - pow(sum_x, 2))
β0 = ((sum_Y*sumatoria_x2)-(sum_x*sumatoria_xiyi))/((n*sumatoria_x2)-pow(sum_x,2))
print("Ecuación de regresión: Y = {:.2f} + {:.2f}X".format(β0, β1))

# Predicción para X = 800
prediccion = β0 + β1 * 800
print("Predicción para X = 800: Y = {:.2f}".format(prediccion))

# Graficar datos y línea de regresión
plt.scatter(x, y, color='blue', label='Datos')
plt.plot(x, [β0 + β1 * xi for xi in x], color='red', label='Línea de regresión')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regresión lineal')
plt.legend()
plt.show()
print(df,sumatoria_xiyi,sumatoria_x2,β1,β0)
