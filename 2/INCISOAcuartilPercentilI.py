import pandas as pd
from google.colab import drive
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
drive.mount('/content/drive')

df = pd.read_csv('/content/drive/My Drive/Pokemon.csv',delimiter=';')
#print(df)

#CALCULANDO LOS PERCENTILES DE CADA COLUMNA (FUNCION MAS ABAJO)

columnaTotal = 'Total'  
valoresTotal = df[columnaTotal].dropna().tolist()

p90t = calcular_percentil(valoresTotal, 50)
print("El percentil de la columna 'Total' es:", p90t)

columnaHP='HP'
valoresHP = df[columnaHP].dropna().tolist()

p90hp = calcular_percentil(valoresHP, 50)
print("El percentil de la columna 'HP' es:", p90hp)

columnaAttack='Attack'
valoresAttack = df[columnaAttack].dropna().tolist()

p90attack = calcular_percentil(valoresAttack, 50)
print("El percentil de la columna 'Attack' es:", p90attack)

columnaDefense='Defense'
valoresDefense = df[columnaDefense].dropna().tolist()

p90defense = calcular_percentil(valoresDefense, 50)
print("El percentil de la columna 'Defense' es:", p90defense)

columnaspattack='Sp. Atk'
valorespattack = df[columnaspattack].dropna().tolist()

p90spattack = calcular_percentil(valorespattack, 50)
print("El percentil de la columna 'Sp. Atk' es:", p90spattack)

columnaspdefense='Sp. Def'
valoresspdefense = df[columnaspdefense].dropna().tolist()

p90spdefense = calcular_percentil(valoresspdefense, 50)
print("El percentil de la columna 'Sp. Def' es:", p90spdefense)

columnaSpeed='Speed'
valoresSpeed = df[columnaSpeed].dropna().tolist()

p90speed = calcular_percentil(valoresSpeed, 50)
print("El percentil de la columna 'Speed' es:", p90speed)

#CALCULANDO LOS CUARTILES DE CADA COLUMNA

print(calcular_cuartiles(valoresHP), "para HP")
print(calcular_cuartiles(valoresAttack),"para Attack")
print(calcular_cuartiles(valoresDefense),"para Defense")
print(calcular_cuartiles(valorespattack),"para Sp. Atk")
print(calcular_cuartiles(valoresspdefense),"para Sp. Def")
print(calcular_cuartiles(valoresSpeed),"para Speed")

def calcular_percentil(valores, percentil): #aqui el percentil se cambia por el numero deseado
    # Ordenar los valores de menor a mayor
    valores_ordenados = sorted(valores)

    # Índice del percentil
    k = (len(valores_ordenados) - 1) * (percentil / 100.0)

    # Obtener la parte entera y decimal del índice
    f = int(k)
    c = k - f


    if f + 1 < len(valores_ordenados):
        resultado = valores_ordenados[f] + c * (valores_ordenados[f + 1] - valores_ordenados[f])
    else:
        resultado = valores_ordenados[f]

    return resultado

def calcular_cuartiles(datos):
    Q1 = calcular_percentil(datos, 25)
    Q2 = calcular_percentil(datos, 50)  # Mediana
    Q3 = calcular_percentil(datos, 75)
    return Q1, Q2, Q3