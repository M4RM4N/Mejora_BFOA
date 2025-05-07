import pandas as pd

# Cargar los archivos CSV
original = pd.read_csv('resultados_bfoa.csv')
mejorado = pd.read_csv('resultados_bfoa2.csv')

# Calcular estadísticas descriptivas para ambos conjuntos
estadisticas_original = original.describe()
estadisticas_mejorado = mejorado.describe()

# Unir las estadísticas lado a lado para comparación
comparacion = pd.concat([estadisticas_original, estadisticas_mejorado], axis=1, keys=["Original", "Mejorado"])
comparacion

