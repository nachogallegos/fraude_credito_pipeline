from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from datetime import datetime

# Configuración del DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 2, 22),
    'retries': 1,
}

dag = DAG(
    'fraude_credito_pipeline',
    default_args=default_args,
    schedule_interval=None,  # Ejecutar bajo demanda
)

# Tarea para extraer datos de BigQuery
extract_data = BigQueryInsertJobOperator(
    task_id='extraer_datos',
    sql="""
        SELECT Time, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, 
               V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28, Amount, Class
        FROM `deteccion-fraude-transacciones.fraude_credito.transacciones_credito`
    """,
    destination_dataset_table='deteccion-fraude-transacciones.fraude_credito.transacciones_credito',
    use_legacy_sql=False,
    dag=dag,
)
