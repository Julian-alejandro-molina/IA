import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
'''
value_n_list = ['Andrew', 'Phillip', 'John']
print(value_n_list)
value_w_list = [50,         78,      91.5] 
value_h_list = [1.76,      1.87,     1.69]
data_dict = {"name":value_n_list,
             "weight":value_w_list,
             "height":value_h_list} #,
print(data_dict)
df=pd.DataFrame(data_dict)
print(df)
df['bmi'] = df['weight'] / (df['height'] ** 2)
print(df)
'''
x=[2,3,5,4,9,6,9]
y=[7,5,6,9,4,5,9]
productos = [a * b for a, b in zip(x, y)]
x_cuadrado=[ a*a for a,a in zip(x,x)]
n=7
df = pd.DataFrame({'X':x, 'Y':y, 'Xy':productos, 'x^2':x_cuadrado,})
sumatoria_Xy=df['Xy'].sum()
sumatoria_X=df['X'].sum()
sumatoria_y=df['Y'].sum()
sumatoria_Xcuadrado=df['x^2'].sum()
#------------------------------------
resultadouno=(n*sumatoria_Xy)-(sumatoria_X*sumatoria_y)
resultadodos = (n * sumatoria_Xcuadrado) - pow(sumatoria_X, 2)
resultadoFinaluno=resultadouno/resultadodos
#-----------------------------------------
resultadotres=(sumatoria_y/n)-(resultadouno/resultadodos)*(sumatoria_X/n)

print(df,sumatoria_Xy,sumatoria_X,sumatoria_y,sumatoria_Xcuadrado,resultadouno,resultadodos,resultadoFinaluno,resultadotres)
plt.figure(figsize=(10, 6))

# Scatter plot de los datos originales
plt.scatter(x, y, color='blue', label='Datos originales')

# Crear la línea de regresión
x_vals = np.array(x)
y_vals = resultadoFinaluno * x_vals + resultadotres

# Graficar la línea de regresión
plt.plot(x_vals, y_vals, color='red', label='Línea de regresión')

# Configuración de la gráfica
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico de datos con línea de regresión')
plt.legend()
plt.grid(True)
plt.show()
