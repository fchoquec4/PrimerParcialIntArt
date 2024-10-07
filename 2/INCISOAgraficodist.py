import matplotlib.pyplot as plt
import seaborn as sns


fig, axes = plt.subplots(3, 2, figsize=(12, 10))
columnas_numericas = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']

for i, columna in enumerate(columnas_numericas):
    sns.histplot(df[columna].dropna(), kde=True, ax=axes[i//2, i%2], color='blue')
    axes[i//2, i%2].set_title(f'Distribución de {columna}')

plt.tight_layout()
plt.show()
