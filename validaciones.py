def validar_vacio(dato):
    return dato.strip() != ""


def validar_dato(dato):
    return validar_vacio(dato)


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