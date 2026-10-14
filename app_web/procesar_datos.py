
import sys

from datos import cargar_json, filtrar_datos, validar_mediciones, validar_estacion
from estadisticas import calcular_estadisticas
from graficos import generar_grafico


def guardar_csv(registros, estacion, medicion):
    if len(registros) == 0:
        print("No hay registros para guardar.")
        return

    nombre_archivo = "salidas/" + estacion.replace(" ", "_") + "_" + medicion + ".csv" 

    archivo = open(nombre_archivo, "w")

    encabezados = list(registros[0].keys())
    archivo.write(",".join(encabezados) + "\n")

    for registro in registros:
        valores = []

        for campo in encabezados:
            valores.append(str(registro[campo]))

        archivo.write(",".join(valores) + "\n")

    archivo.close()

    print("Archivo CSV guardado en:", nombre_archivo)


def main():
    if len(sys.argv) != 4:
        print("Uso: python procesar_datos.py ruta_json estacion medicion")
        return

    ruta_json = sys.argv[1]
    estacion = sys.argv[2]
    medicion = sys.argv[3]

    # Validar la medicion antes de procesar los datos
    if not validar_mediciones(medicion):
        print("Error: medicion no valida.")
        print("Opciones: temperatura, humedad, presion, direccion, velocidad")
        return

    try:
        datos = cargar_json(ruta_json)
    except FileNotFoundError:
        print("Error: no se encontro el archivo JSON.")
        return
    if not validar_estacion(datos, estacion):
        print("Error: la estacion ingresada no existe en el JSON.")
        return
    filtrados = filtrar_datos(datos, estacion, medicion)

    estadisticas = calcular_estadisticas(filtrados, medicion)

    print("Primeros registros encontrados:")
    for registro in filtrados[:5]:
        print(registro)

    print("Estacion:", estacion)
    print("Medicion:", medicion)

    if len(filtrados) > 0:
        print("Cantidad:", estadisticas["cantidad"])
        print("Minimo:", estadisticas["minimo"])
        print("Maximo:", estadisticas["maximo"])
        print("Promedio:", round(estadisticas["promedio"], 2))
    else:
        print("No se encontraron registros para esa estacion.")

    guardar_csv(filtrados, estacion, medicion)
    generar_grafico(filtrados, estacion, medicion)


if __name__ == "__main__":
    main()
