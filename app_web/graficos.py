import matplotlib.pyplot as plt


def generar_grafico(registros, estacion, medicion):
    if len(registros) == 0:
        print("No hay registros para generar el grafico.")
        return

    horas = []
    valores = []

    for registro in registros:
        horas.append(registro["hora"])
        valores.append(float(registro[medicion]))

    plt.plot(horas, valores, marker="o")

    plt.title(estacion + " - " + medicion)
    plt.xlabel("Hora")
    plt.ylabel(medicion)

    plt.grid(True)
    plt.tight_layout()

    nombre_archivo = "salidas/" + estacion.replace(" ", "_") + "_" + medicion + ".png"

    plt.savefig(nombre_archivo)
    plt.close()

    print("Grafico guardado en:", nombre_archivo)