import time

import pandas as pd
import psycopg2
from src.log_config import logger

process_date = time.strftime('%d-%m-%Y')
xlsx_file = f'backup-saft-{process_date}.xlsx' # Change this for the real file
sheet_name = 'Sheet1'
dbname = 'bd_saftonline'
user = 'user'
password = 'password123'
host = '192.168.1.99'
port = '5432'

table_name = 't_saftonline'
primary_key = 'Empresa.Emp_NIF'

try:
    df = pd.read_excel(xlsx_file, sheet_name=sheet_name)
    logger.info('Excel file read successfully.')
except Exception as e:
    logger.error('Error on read excel file:', e)
    exit(1)

escaped_columns = [f'"{col}"' for col in df.columns]
placeholders = ', '.join(['%s'] * len(df.columns))

update_columns = [f'"{col}"' for col in df.columns if col != primary_key]
update_clause = ', '.join(
    [f'{col} = EXCLUDED.{col}' for col in update_columns]
)

query = f"""
INSERT INTO {table_name} ({', '.join(escaped_columns)})
VALUES ({placeholders})
ON CONFLICT ("{primary_key}") DO UPDATE SET {update_clause};
"""

try:
    conn = psycopg2.connect(
        dbname=dbname, user=user, password=password, host=host, port=port
    )
    cursor = conn.cursor()
    logger.info('Connection to the PostgreSQL established successfully!')
except Exception as e:
    logger.error('Error to connect with PostgresSQL:', e)
    exit(1)

try:
    for index, row in df.iterrows():
        values = tuple(row[col] for col in df.columns)
        cursor.execute(query, values)
    conn.commit()
    logger.info('Data updated/insert successfully!')
except Exception as e:
    logger.error('Error to updated/insert the data:', e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()
