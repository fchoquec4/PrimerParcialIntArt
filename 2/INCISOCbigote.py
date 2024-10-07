columnas = ['HP', 'Attack', 'Defense']

# Calcular media, mediana y moda
media = df[columnas].mean()
mediana = df[columnas].median()
moda = df[columnas].mode().iloc[0]

print("Media:\n", media)
print("\nMediana:\n", mediana)
print("\nModa:\n", moda)

# Crear el gráfico de cajas y bigotes
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[columnas])
plt.title('Diagrama de Cajas y Bigotes para HP, Attack, y Defense')
plt.xlabel('Estadísticas')
plt.ylabel('Valores')
plt.show()