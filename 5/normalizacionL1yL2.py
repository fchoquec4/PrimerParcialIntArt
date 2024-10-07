
import pandas as pd
from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('/content/drive/My Drive/Pokemon.csv',delimiter=';')

#PENALIZACION
c = df['HP'].tolist()

#L1
def penalizacion_L1(coeficientes, lambda_val):
    l1_penalizacion = 0
    for w in coeficientes:
        l1_penalizacion += abs(w)
    return lambda_val * l1_penalizacion
#L2
def penalizacion_L2(coeficientes, lambda_val):
    l2_penalizacion = 0
    for w in coeficientes:
        l2_penalizacion += w ** 2
    return lambda_val * l2_penalizacion


lambda_val = 0.05


penalizacion_l1 = penalizacion_L1(c, lambda_val)
penalizacion_l2 = penalizacion_L2(c, lambda_val)


print("L1:", penalizacion_l1)
print("L2:", penalizacion_l2)