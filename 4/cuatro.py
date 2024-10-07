import pandas as pd
from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('/content/drive/My Drive/Pokemon.csv',delimiter=';')


#Iniciando con el preprocesamiento, primero se llenan los espacios vacios de Type 2 por No Type


df['Type 2'] = df['Type 2'].fillna('No Type')

pd.set_option('display.max_rows', None)  # Muestra todas las filas
pd.set_option('display.max_columns', None)  # Muestra todas las columnas
pd.set_option('display.width', None)  # Ajusta el ancho de la visualización
#print(df)
print("----------")

#onehotencoder, labelencoder, discretización y normalización.

#USAREMOS LABELENCODER EN LAS COLUMNAS DE AMBOS TIPOS DE POKEMON, QUE SON 18 EN TOTAL, EN LA COLUMNA DE TYPE2 SERAN 19 YA QUE CONTAREMOS EL No Type

from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()

df['Type 1'] = label_encoder.fit_transform(df['Type 1'])
df['Type 2'] = label_encoder.fit_transform(df['Type 2'])

#print(df)

#AHORA USAREMOS ONEHOTENCONDER PARA LA COLUMNA DE Legendary, QUE SOLO TIENE 2 POSIBLES VALORES

from sklearn.preprocessing import OneHotEncoder

# Supongamos que 'df' es tu DataFrame original

# Crear el OneHotEncoder
ohe = OneHotEncoder(sparse_output=False)  # Cambia sparse por sparse_output

# Transformar la columna 'Legendary'
legendary_encoded = ohe.fit_transform(df[['Legendary']])

# Crear un DataFrame a partir del resultado
legendary_df = pd.DataFrame(legendary_encoded, columns=ohe.get_feature_names_out(['Legendary']))

# Concatenar el nuevo DataFrame al original
df = pd.concat([df, legendary_df], axis=1)


df.drop('Legendary', axis=1, inplace=True)

#print(df)

#AHORA APLICAREMOS LA DISCRETIZACION

from sklearn.preprocessing import KBinsDiscretizer

# Definir las características que deseas discretizar
features = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
X = df[features]

# Aplicar KBinsDiscretizer para discretizar en 5 bins (por ejemplo)
discretizer = KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='uniform')
X_discretized = discretizer.fit_transform(X)

# Crear un DataFrame con los valores discretizados
X_discretized_df = pd.DataFrame(X_discretized, columns=features)

# Reemplazar las columnas originales con las discretizadas
df[features] = X_discretized_df

#print(df)

#POR ULTIMO LA NORMALIZACION

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

# Aplicamos la normalización a las columnas seleccionadas
df[features] = scaler.fit_transform(df[features])

# Imprimir las primeras filas del dataframe normalizado
print(df[features])