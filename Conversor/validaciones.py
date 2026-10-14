def validar_vacio(dato):
    return dato.strip() != ""


def es_numero(dato):
    try:
        float(dato)
        return True
    except ValueError:
        return False


def hora_valida(hora):
    if not es_numero(hora):
        return False

    hora = int(hora)

    return 0 <= hora <= 23


def humedad_valida(humedad):
    if not es_numero(humedad):
        return False

    humedad = float(humedad)

    return 0 <= humedad <= 100


def direccion_valida(direccion):
    if not es_numero(direccion):
        return False

    direccion = float(direccion)

    return 0 <= direccion <= 360


def velocidad_valida(velocidad):
    if not es_numero(velocidad):
        return False

    velocidad = float(velocidad)

    return velocidad >= 0


def fecha_valida(fecha):
    if len(fecha) != 8:
        return False

    if not es_numero(fecha):
        return False

    dia = int(fecha[0:2])
    mes = int(fecha[2:4])
    anio = int(fecha[4:8])

    if mes < 1 or mes > 12:
        return False

    if mes == 2:
        dias = 28
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dias = 30
    else:
        dias = 31

    if dia < 1 or dia > dias:
        return False

    if anio < 1:
        return False

    return True

def temperatura_valida(temperatura):
    return es_numero(temperatura)


def presion_valida(presion):
    return es_numero(presion)


def estacion_valida(estacion):
    return validar_vacio(estacion)