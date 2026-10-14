import sys
import json


from validaciones import (
    fecha_valida,
    hora_valida,
    temperatura_valida,
    humedad_valida,
    presion_valida,
    direccion_valida,
    velocidad_valida,
    estacion_valida
)


if len(sys.argv) < 3:
    print("Faltan argumentos.")
    print("Uso tiene que ser: python datos.py archivo.txt archivo.json")
    sys.exit()
    
def validar_registro(registro):
#Esto sirve para que si alguien escribe solamente desde la terminal:
#python datos.py
#el programa no se rompa


    #lista_incorrectos = []

    if len(registro) < 8:
        #lista_incorrectos.append("registro incorrecto")
        return "Registro incompleto"

    if not fecha_valida(registro[0]):
        return "Fecha incorrecta"

    if not hora_valida(registro[1]):
        return "Hora incorrecta"

    if not temperatura_valida(registro[2]):
        return "Temperatura incorrecta"

    if not humedad_valida(registro[3]):
        return "Humedad incorrecta"

    if not presion_valida(registro[4]):
        return "Presion incorrecta"

    if not direccion_valida(registro[5]):
        return "Direccion incorrecta"

    if not velocidad_valida(registro[6]):
        return "Velocidad incorrecta"

    estacion = " ".join(registro[7:])

    if not estacion_valida(estacion):
        return "Estacion incorrecta"

    return ""
    #if lista_incorrectos.len >= 1
    


def convertir_registro(registro):

    estacion = " ".join(registro[7:])

    nuevo_registro = {
        "fecha": registro[0],
        "hora": registro[1],
        "temperatura": registro[2],
        "humedad": registro[3],
        "presion": registro[4],
        "direccion": registro[5],
        "velocidad": registro[6],
        "estacion": estacion
    }

    return nuevo_registro


try:
    archivo = open(sys.argv[1], "r") #esto interactua con el TXT y lo lee
except: 
    print("No se pudo abrir el archivo de entrada, verifique si existe")
    print()
    sys.exit()
#Esto nos ayuda que si el txt no existe o no se puede abrir, nos muestre un mensaje 

registros_validos = []
registros_invalidos = []
errores = []
cantidad = 0


for linea in archivo:

    linea = linea.strip()

    if linea != "":

        datos = linea.split()

        if datos[0] != "FECHA" and datos[0] != "[HOA]":

           if len(datos) >= 7 and len(datos[0]) == 8:

              cantidad = cantidad + 1

              error = validar_registro(datos)

              if error == "":
                 registro_nuevo = convertir_registro(datos)
                 registros_validos.append(registro_nuevo)
              else:
                 registros_invalidos.append([linea, error])
                 errores.append(error)

archivo.close()

datos_json = {
    "total_registros": cantidad,
    "registros_validos": len(registros_validos),
    "registros_invalidos": len(registros_invalidos),
    "validos": registros_validos,
    "invalidos": registros_invalidos
}


try:
    salida = open(sys.argv[2], "w") #esto crea el JSON

    json.dump(datos_json, salida, indent=4)
#Lo que hace es tomar el segundo argumento de la terminal.
#sys.argv[0] datos.py
#sys.argv[1] datohorario20260819.txt
#sys.argv[2] observaciones.json
    salida.close()
except:
    print("no se puede crear un archivo de salida.")
    sys.exit()
print("RESUMEN")
print()
print("Cantidad de registros:", cantidad)
print("Registros validos:", len(registros_validos))
print("Registros invalidos:", len(registros_invalidos))

print()
print("ERRORES ENCONTRADOS")
print()


tipos_de_error = []

for error in errores:

    if error not in tipos_de_error:
        tipos_de_error.append(error)



for tipo in tipos_de_error:

    cantidad_error = 0

    for error in errores:

        if error == tipo:
            cantidad_error = cantidad_error + 1

    print(tipo + ":", cantidad_error)