from google.cloud import bigquery

# Conectar a BigQuery
client = bigquery.Client()

# Realizar una consulta simple
query = "SELECT COUNT(*) FROM `deteccion-fraude-transacciones.fraude_credito.transacciones_credito`"
result = client.query(query).result()

# Imprimir el resultado
for row in result:
    print(row)
