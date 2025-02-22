WITH transacciones_fraudulentas AS (
    SELECT *
    FROM {{ ref('transacciones_credito') }}
    WHERE Class = 1
)
SELECT * FROM transacciones_fraudulentas;
