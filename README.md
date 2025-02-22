# Proyecto de Detección de Fraude en Transacciones Bancarias

Este proyecto construye un pipeline de datos para detectar fraudes en transacciones bancarias utilizando el dataset "Credit Card Fraud Detection" de Kaggle.

## Tecnologías Utilizadas:
- **BigQuery**: Almacenamiento y procesamiento de transacciones.
- **DBT**: Transformaciones de datos y creación de modelos de detección de fraude.
- **Airflow**: Orquestación y automatización del pipeline.
- **Python**: Extracción de datos, limpieza y validaciones.
- **GitHub**: Control de versiones y documentación del proyecto.

## Estructura del Proyecto
- `dags/`: Archivos de Airflow.
- `dbt/`: Archivos para la transformación de datos con DBT.
- `scripts/`: Scripts de Python para la extracción y limpieza de datos.

## Cómo Ejecutar el Proyecto
1. Configura Google Cloud, BigQuery, y Airflow.
2. Ejecuta el DAG de Airflow para extraer, transformar y analizar los datos.
