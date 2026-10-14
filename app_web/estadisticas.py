
def calcular_estadisticas(registros, medicion):
    valores = []

    for registro in registros:
        valor = float(registro[medicion])
        valores.append(valor)

    if len(valores) == 0:
        return {}

    cantidad = len(valores)
    minimo = min(valores)
    maximo = max(valores)

    suma = 0

    for valor in valores:
        suma = suma + valor

    promedio = suma / cantidad

    estadisticas = {
        "cantidad": cantidad,
        "minimo": minimo,
        "maximo": maximo,
        "promedio": promedio
    }

    return estadisticas
