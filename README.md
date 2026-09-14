# Trabajo_Integrador2026

## Conversor de archivo TXT a JSON

Este proyecto consiste en desarrollar un programa en Python capaz de leer un archivo de observaciones meteorológicas en formato TXT, validar sus datos y generar un archivo JSON.

El programa permite separar los registros válidos de aquellos que presentan algún error.

## Integrantes

**Grupo:** Los de Pepsi

**Integrantes:**

 Leo Chambilla
 Enzo Jones

## Archivos del proyecto

- `datos.py`: contiene el programa principal.
- `validaciones.py`: contiene las funciones utilizadas para validar los datos.
- `datohorario20260819.txt`: archivo de entrada con las observaciones meteorológicas.
- `observaciones.json`: archivo generado con los resultados.
- `README.md`: documentación del proyecto.

## Requisitos

Para utilizar el programa se necesita utilizar como requisito:

- Una version Python
- Visual Studio Code
- Un entorno virtual de Python (`.venv`)

## Implementar

Desde la terminal, ubicándose en la carpeta del proyecto, se ejecuta:

```text
python datos.py datohorario20260819.txt observaciones.json
