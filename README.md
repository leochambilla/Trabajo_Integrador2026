# Trabajo_Integrador2026

## Descripción del proyecto

Este proyecto consiste en desarrollar un programa en Python capaz de leer un archivo de observaciones meteorológicas en formato TXT, validar sus datos y generar un archivo JSON.

El programa permite separar los registros válidos de aquellos que presentan algún error, indicando el motivo del error. Además, permite procesar los datos válidos para obtener estadísticas y generar archivos de salida.

## Objetivo

El objetivo del programa es interpretar los datos de un archivo TXT y organizarlos en un archivo JSON. También se busca detectar registros que contengan datos incorrectos y conservarlos indicando el motivo del error.

En la segunda parte del trabajo, se utilizan los datos del JSON para filtrar observaciones por estación meteorológica y tipo de medición, calcular estadísticas y generar gráficos.

## Integrantes

**Grupo:** Los de Pepsi

**Integrantes:**
- Leo Chambilla
- Enzo Jones

## Archivos del proyecto

### Conversor

- `Conversor/adaptar_datos.py`: contiene el código relacionado con la adaptación de los datos del archivo TXT.
- `Conversor/validaciones.py`: contiene las funciones utilizadas para validar los datos.
- `Conversor/datohorario20260819.txt`: archivo de entrada con las observaciones meteorológicas.

### Procesamiento de datos

- `app_web/datos/observaciones.json`: contiene los datos meteorológicos en formato JSON.
- `app_web/datos.py`: carga el JSON, filtra los registros y valida la estación y la medición.
- `app_web/estadisticas.py`: calcula la cantidad de registros, el mínimo, el máximo y el promedio.
- `app_web/graficos.py`: genera gráficos de líneas y los guarda en formato PNG.
- `app_web/procesar_datos.py`: permite ejecutar el procesamiento desde la terminal.
- `app_web/salidas/`: carpeta donde se guardan los archivos CSV y los gráficos generados.
- `app_web/app.py`: archivo previsto para desarrollar la aplicación web en la segunda etapa.

## Requisitos

Para utilizar el programa se necesita:

- Python 3.14
- Visual Studio Code, como editor de código.
- Un entorno virtual de Python (`.venv`).
- Matplotlib, para generar los gráficos.

## Ejecución del conversor

Desde la carpeta `Conversor`, se puede ejecutar el conversor indicando el archivo TXT y la ruta de salida del JSON, de acuerdo con los argumentos que acepte el programa:

```bash
python adaptar_datos.py datohorario20260819.txt observaciones.json
```

## Ejecución del procesamiento

Desde la carpeta `app_web`, ejecutar el siguiente comando:

```bash
python procesar_datos.py datos/observaciones.json "AEROPARQUE AERO" temperatura
```

El programa recibe tres argumentos:

1. La ruta del archivo JSON.
2. El nombre de la estación meteorológica.
3. La medición que se desea analizar.

Las mediciones disponibles son:

- `temperatura`
- `humedad`
- `presion`
- `direccion`
- `velocidad`

El programa filtra los registros de la estación seleccionada, muestra los primeros registros encontrados y calcula la cantidad, el valor mínimo, el valor máximo y el promedio de la medición.

También genera un archivo CSV con los registros filtrados y un gráfico de líneas en formato PNG.

## Archivos generados

Los archivos de salida se guardan en la carpeta `app_web/salidas/`:

- Un archivo CSV con los datos filtrados.
- Una imagen PNG con el gráfico de la medición seleccionada.

## Organización del código

El proyecto se divide en módulos para separar las tareas de lectura y adaptación de datos, validación, procesamiento, cálculo de estadísticas y generación de gráficos.

