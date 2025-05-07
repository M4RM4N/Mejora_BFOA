import subprocess
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

resultados = []

for i in range(30):
    print(f"Ejecutando corrida {i+1}...")
    result = subprocess.run(
        ["python", "parallel_BFOA.py"],
        capture_output=True,
        text=True
    )
    output = result.stdout

    # Buscar línea con fitness y blosum
    match = re.search(r"Best:\s+(\d+)\s+Fitness:\s+([\d\.]+)\s+BlosumScore\s+([\d\.]+)", output)
    tiempo_match = re.search(r"--- ([\d\.]+) seconds ---", output)

    if match and tiempo_match:
        iter_optima = int(match.group(1))
        fitness = float(match.group(2))
        blosum = float(match.group(3))
        tiempo = float(tiempo_match.group(1))

        resultados.append([i+1, fitness, tiempo, iter_optima, blosum])
    else:
        print(f"[!] Error en corrida {i+1}: no se encontraron datos.")

# Guardar resultados
df = pd.DataFrame(resultados, columns=["Corrida", "Fitness", "Tiempo (s)", "Iteración óptima", "BLOSUM score"])
df.to_csv("resultados_bfoa2.csv", index=False)
print(df)

# Gráficos
sns.boxplot(y=df["Fitness"])
plt.title("Distribución del Fitness en 30 Corridas")
plt.show()

plt.plot(df["Corrida"], df["Tiempo (s)"], marker='o')
plt.title("Tiempo de Ejecución por Corrida")
plt.xlabel("Corrida")
plt.ylabel("Tiempo (s)")
plt.grid(True)
plt.show()

sns.scatterplot(data=df, x="Iteración óptima", y="BLOSUM score")
plt.title("BLOSUM Score vs Iteración Óptima")
plt.show()
