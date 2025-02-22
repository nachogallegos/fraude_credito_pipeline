from google.cloud import bigquery
import pandas as pd

# Conectar a BigQuery
client = bigquery.Client()

# Definir la consulta
query = """
    SELECT Time, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, 
           V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28, Amount, Class
    FROM `deteccion-fraude-transacciones.fraude_credito.transacciones_credito`
"""

# Ejecutar la consulta y cargar los datos en un DataFrame de Pandas
df = client.query(query).to_dataframe()

# Convertir la columna 'Time' a STRING para evitar problemas con la notación científica
df['Time'] = df['Time'].apply(lambda x: str(x))

# Verificar si hay valores nulos
print(df.isnull().sum())

# Eliminar valores nulos o realizar otras transformaciones necesarias
df = df.dropna()

# Guardar el archivo limpio (si es necesario)
df.to_csv('transacciones_limpias.csv', index=False)
