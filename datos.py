import sys
from validaciones import validar_vacio


def obtener_registros(nombre_archivo):
    registros = []

    with open(nombre_archivo, "r", encoding="latin-1") as archivo:
        for linea in archivo:
            linea = linea.strip()

            if not validar_vacio(linea):
                continue

            if linea.startswith("FECHA"):
                continue

            partes = linea.split()

            if len(partes) >= 7:
                registros.append(partes)

    return registros


def mostrar_registros(registros):
    print("Cantidad de registros leídos:", len(registros))

    for registro in registros[:5]:
        print(registro)


if len(sys.argv) < 2:
    print("Uso: python adaptar_datos.py datohorario20260819.txt")
else:
    nombre_archivo = sys.argv[1]

    datos = obtener_registros(nombre_archivo)

    mostrar_registros(datos)