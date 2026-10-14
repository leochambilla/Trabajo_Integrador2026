
import json


def cargar_json(ruta):
    with open(ruta, "r") as archivo:
        datos = json.load(archivo)

    return datos


def filtrar_datos(datos, estacion, medicion):
    registros_validos = datos["validos"]
    filtrados = []

    for registro in registros_validos:
        if registro["estacion"] == estacion:
            if medicion in registro:
                filtrados.append(registro)

    return filtrados

def validar_mediciones(medicion):
    mediciones = ["temperatura", "humedad", "presion", "direccion", "velocidad"]

    if medicion in mediciones:
        return True
    else:
        return False

def validar_estacion(datos, estacion):
    registros_validos = datos["validos"]

    for registro in registros_validos:
        if registro["estacion"] == estacion:
            return True

    return False

